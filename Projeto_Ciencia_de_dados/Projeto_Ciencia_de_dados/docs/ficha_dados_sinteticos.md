# Ficha dos dados sintéticos

**Arquivos:** `dados/sintetico_ticKids2025_familias.csv` (2.400 registros) e `dados/sintetico_validacao_marginais.csv` (26 linhas).
**Gerador:** `scripts/criar_dados_sinteticos.py` (semente 2025, então dá o mesmo resultado toda vez).

## Por que criamos

O projeto precisa de pelo menos 1.000 registros para treinar e testar modelos (agrupamento e classificação). Não conseguimos os microdados do TIC Kids Online
Brasil 2025, e o questionário do nosso TCC ainda depende de aprovação do CEP. Os dados sintéticos servem para treinar o método sem coletar
dados de crianças e adolescentes.

## O que é cada registro

Uma criança ou adolescente **fictício** de 9 a 17 anos. As colunas são: `id_sintetico`, `faixa_etaria` (9-10, 11-12, 13-14, 15-17), três indicadores de mediação
(`med_regras_celular`, `med_olha_celular`, `med_sem_celular`), três de exposição (`exp_ia_generativa`, `exp_pesquisou_produtos`, `exp_compras`),
`usa_recurso_limite_tempo`, `conversa_sobre_online` e `sintetico` (sempre `True`). Os indicadores valem 0 ou 1.

## Como geramos

1. **Faixas e tamanhos.** 600 registros por faixa etária (a pesquisa de verdade entrevistou 2.370). A distribuição por idade não representa a população.
2. **Percentuais.** Para cada indicador e faixa, o número de "sim" é o percentual publicado (`dados/ticKids2025_por_faixa_etaria.csv`) vezes 600. Por isso os
   percentuais sintéticos batem com os publicados (diferença máxima de 0,00 p.p.).
3. **Recurso técnico (37%) e diálogo (44%).** Só existe o total nacional, sem recorte por idade. Usamos o mesmo percentual em todas as faixas, o que é uma simplificação.
4. **Relação entre os indicadores (suposição nossa).** Cada registro recebe um "perfil" de mediação e outro de exposição. Os indicadores de mediação e o uso de
   recurso técnico andam com o perfil de mediação, e os de exposição andam com o de exposição. A força dessa ligação é definida pelos parâmetros `carga_indic` (0,6),
   `carga_recurso` (0,6), `carga_conversa` (0,4) e `rho` (0, ou seja, sem relação entre mediação e exposição). Esses valores foram escolhas nossas e não medidas.

## O que a validação garante e o que não garante

- Garante que os percentuais por faixa são iguais aos publicados, que não há valores ausentes, que os ids são únicos e que todos os registros estão marcados como sintéticos
  (verificações S1 a S4 da Fase 2 do notebook).
- Não garante que a relação entre os indicadores exista na vida real. Na análise de sensibilidade (Fase 4), a AUC da previsão do uso de recurso técnico
  vai de 0,49 a 0,87 só por mudar essas suposições.

## Cuidados éticos

- Não criamos nem usamos dado pessoal: sem nome, escola, cidade, contato, data de nascimento ou qualquer identificador.
- Nenhum registro vem de uma pessoa real. A única entrada são percentuais públicos agregados.
- Como não existe uma pessoa por trás de cada linha, não há risco de identificar alguém.
- Os parâmetros e limites estão descritos aqui e no notebook, para ninguém confundir os dados com uma pesquisa.

## O que pode e o que não pode

| Pode | Não pode |
|---|---|
| Treinar K-means, classificação e divisão em treino e teste | Citar como resultado de pesquisa sobre famílias reais |
| Testar o quanto as conclusões dependem das suposições | Usar para estimar prevalências ou afirmar algo no TCC sobre crianças e adolescentes |
| Deixar o código pronto para os microdados reais | Misturar com dados reais sem a coluna `sintetico` |

## Como declarar no trabalho

> "Os microdados do TIC Kids 2025 não estavam disponíveis. Para testar o método de agrupamento e classificação, geramos 2.400 registros sintéticos a partir
> dos percentuais públicos da pesquisa. Os resultados dessa etapa mostram como o método funciona e o quanto ele depende das suposições do gerador.
> Eles não são evidência sobre famílias reais."

## Quando trocar pelos dados reais

Quando conseguirmos os microdados do Cetic.br, é só trocar o arquivo `sintetico_ticKids2025_familias.csv` pelos dados reais (mantendo os nomes das colunas), rodar o
notebook de novo e comparar a AUC e a silhueta com os valores sintéticos.
