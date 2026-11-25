"""
Gera 2.400 registros sintéticos (inventados) para o projeto de Ciência de Dados.

Cada linha é uma criança ou adolescente fictício de 9 a 17 anos. Ninguém é real e não existe nenhum dado pessoal aqui (nada de nome,
escola, cidade ou contato).

Como funciona: o script lê os percentuais públicos do TIC Kids Online Brasil 2025 que já estão em dados/ticKids2025_por_faixa_etaria.csv
e cria registros que repetem exatamente esses percentuais em cada faixa etária. A única coisa que é suposição nossa é a relação entre os
indicadores (quem tem mais mediação num indicador tende a ter nos outros). Ela é controlada pelos parâmetros "carga_*" e a gente testa
o que acontece quando mudam, na análise de sensibilidade do notebook.

Importante: isso não são os microdados do Cetic.br e não serve para concluir nada sobre famílias reais. Serve para treinar o método
(agrupamento e classificação). Mais detalhes em docs/ficha_dados_sinteticos.md.

Para rodar:  python scripts/criar_dados_sinteticos.py
"""
from pathlib import Path
import numpy as np
import pandas as pd

RAIZ = Path(__file__).resolve().parents[1]
DADOS = RAIZ / "dados"

IDADES = ["9-10", "11-12", "13-14", "15-17"]
N_POR_FAIXA = 600          # 4 faixas x 600 = 2.400 registros (a pesquisa de verdade entrevistou 2.370)
SEMENTE = 2025

# indicador publicado (nome na tabela do TIC Kids) -> nome da coluna sintética
INDICADORES = {
    "Pais colocam regras para usar o celular": "med_regras_celular",
    "Pais olham o celular (com quem fala / o que faz)": "med_olha_celular",
    "Pais deixam sem usar o celular por algum tempo": "med_sem_celular",
    "Usou IA generativa (ao menos uma atividade)": "exp_ia_generativa",
    "Pesquisou produtos na Internet para comprar": "exp_pesquisou_produtos",
    "Realizou compras na Internet": "exp_compras",
}
MED = ["med_regras_celular", "med_olha_celular", "med_sem_celular"]
EXP = ["exp_ia_generativa", "exp_pesquisou_produtos", "exp_compras"]
# só existe o total nacional (sem recorte por idade), então usamos o mesmo valor em todas as faixas
P_RECURSO_TEMPO = 37       # responsáveis que usam recurso técnico que limita o tempo na Internet
P_CONVERSA = 44            # responsáveis que conversam sobre o que o filho faz na Internet


def _marca_topo(score: np.ndarray, p_pct: float) -> np.ndarray:
    """Marca 1 para os k maiores scores, com k = p% do grupo. Assim o percentual fica exato e a correlação é mantida."""
    k = int(round(p_pct / 100 * len(score)))
    x = np.zeros(len(score), dtype=int)
    x[np.argsort(-score)[:k]] = 1
    return x


def gerar(n_por_faixa=N_POR_FAIXA, semente=SEMENTE, carga_indic=0.6, carga_recurso=0.6,
          carga_conversa=0.4, rho=0.0, dados=DADOS) -> pd.DataFrame:
    """Gera os registros sintéticos.

    carga_indic     o quanto cada indicador anda com o "perfil" de mediação ou de exposição (de 0 a 1)
    carga_recurso   o quanto o uso de recurso técnico anda com o perfil de mediação
    carga_conversa  o quanto o diálogo anda com o perfil de mediação
    rho             correlação entre o perfil de mediação e o de exposição (0 = nenhuma)
    """
    pub = pd.read_csv(Path(dados) / "ticKids2025_por_faixa_etaria.csv")
    pub = pub[pub.grupo.isin(IDADES)].pivot(index="indicador", columns="grupo", values="valor_pct")
    rng = np.random.default_rng(semente)
    blocos = []
    for g in IDADES:
        n = n_por_faixa
        z = rng.multivariate_normal([0, 0], [[1, rho], [rho, 1]], size=n)
        z_med, z_exp = z[:, 0], z[:, 1]
        ruido = lambda: rng.standard_normal(n)
        col = {}
        for nome, c in INDICADORES.items():
            lat = z_med if c in MED else z_exp
            col[c] = _marca_topo(carga_indic * lat + np.sqrt(1 - carga_indic**2) * ruido(), pub.loc[nome, g])
        col["usa_recurso_limite_tempo"] = _marca_topo(
            carga_recurso * z_med + np.sqrt(1 - carga_recurso**2) * ruido(), P_RECURSO_TEMPO)
        col["conversa_sobre_online"] = _marca_topo(
            carga_conversa * z_med + np.sqrt(1 - carga_conversa**2) * ruido(), P_CONVERSA)
        blocos.append(pd.DataFrame({"faixa_etaria": g, **col}))
    df = pd.concat(blocos, ignore_index=True)
    df = df.sample(frac=1, random_state=semente).reset_index(drop=True)      # embaralha as linhas
    df.insert(0, "id_sintetico", [f"S{i:04d}" for i in range(1, len(df) + 1)])
    df["sintetico"] = True
    return df


def validar(df: pd.DataFrame, dados=DADOS) -> pd.DataFrame:
    """Compara o percentual sintético com o publicado, por indicador e faixa etária."""
    pub = pd.read_csv(Path(dados) / "ticKids2025_por_faixa_etaria.csv")
    pub = pub[pub.grupo.isin(IDADES)].set_index(["indicador", "grupo"]).valor_pct
    linhas = []
    for nome, c in INDICADORES.items():
        for g in IDADES:
            sint = df.loc[df.faixa_etaria == g, c].mean() * 100
            linhas.append(dict(indicador=nome, faixa_etaria=g, publicado_pct=pub[(nome, g)],
                               sintetico_pct=round(sint, 2), diferenca_pp=round(sint - pub[(nome, g)], 2)))
    for nome, c, p in [("Recurso técnico que limita o tempo na Internet (total)", "usa_recurso_limite_tempo", P_RECURSO_TEMPO),
                       ("Pais conversam sobre o que o filho faz na Internet (total)", "conversa_sobre_online", P_CONVERSA)]:
        sint = df[c].mean() * 100
        linhas.append(dict(indicador=nome, faixa_etaria="Total", publicado_pct=p,
                           sintetico_pct=round(sint, 2), diferenca_pp=round(sint - p, 2)))
    return pd.DataFrame(linhas)


if __name__ == "__main__":
    df = gerar()
    df.to_csv(DADOS / "sintetico_ticKids2025_familias.csv", index=False)
    val = validar(df)
    val.to_csv(DADOS / "sintetico_validacao_marginais.csv", index=False)
    print(f"{len(df)} registros sintéticos gerados | maior diferença vs. publicado: {val.diferenca_pp.abs().max():.2f} p.p.")
