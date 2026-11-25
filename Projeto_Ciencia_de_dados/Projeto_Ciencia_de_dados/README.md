# Controle parental: proteção infantojuvenil no mundo digital
### Análise de dados com CRISP-DM (SaferNet e TIC Kids Online Brasil 2025)

Projeto de **Ciência de Dados e Aprendizagem de Máquina** (UDF), baseado no nosso TCC *Controle parental: proteção infantojuvenil no mundo digital*.
Seguimos o Guia Prático CRISP-DM da Profa. Kadidja Valéria: em cada fase do notebook aparecem o objetivo central, o checklist de execução e a aplicação no projeto.

[![Abrir no Google Colab]([https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/alvarengagraziela3-oss/Ciencia_Dados_Aprendizagem_Maquina/blob/main/Projeto_Ciencia_de_dados/notebooks/crispdm_controle_parental.ipynb])

**Integrantes:**
Graziela Marcela Alvarenga Silva Viana

Gabriela Marcela Alvarenga Silva Viana


## Perguntas de análise

| Pergunta | Responsável | Técnica | Resposta |
|---|---|---|---|
| **P1.** A série de denúncias de imagens de abuso e exploração sexual infantil (SaferNet, 2006–2025) pode ser projetada com uma tendência simples? | Graziela | Regressão linear e validação com origem móvel | **Não.** Os três previsores empatam com o modelo ingênuo (MAE de 8,4 a 8,7 mil denúncias) |
| **P2.** Em que faixa etária a mediação parental fica atrás da exposição e da autonomia digital? | Gabriela | Índices por faixa etária, regressão linear e análise de sensibilidade | **Não há ponto de corte único.** Aos 15–17 anos a exposição supera a mediação nos 9 pares testados |
| **P3.** Com microdados **sintéticos** (2.400 registros), o método agrupa famílias em perfis de mediação e prevê quem usa recurso técnico para limitar o tempo? | Ambas (a definir) | K-means; regressão logística e floresta aleatória com treino e teste | **Sim, mas só em dados sintéticos.** O resultado depende das suposições que fizemos (AUC de 0,49 a 0,87) |

## Principais resultados

| Resultado | Valor | Fonte |
|---|---|---|
| Denúncias novas de imagens de abuso e exploração sexual infantil, 2025 | 63.214 (+19,3% sobre 2024) | SaferNet |
| Pico histórico da série | 71.867 em 2023 | SaferNet |
| 2025 em relação a 2019 | 2,48x (CAGR de 16,3% ao ano) | Notebook, Fase 3 |
| Tendência log-linear 2019–2025 | 12,5% ao ano, R² 0,56, n = 7 | Notebook, Fase 4 |
| Erro (MAE) da validação 2012–2025: ingênuo · média 3 anos · tendência linear | 8.558 · 8.408 · 8.685 | Notebook, Fase 4 |
| Faixa de referência para 2026 (não é previsão confiável) | 62.693 a 65.803, erro típico ≈ 8,4 mil | Notebook, Fase 4 |
| Mediação restritiva (IMR) por faixa: 9–10 · 11–12 · 13–14 · 15–17 | 43 · 44 · 30 · 15 | TIC Kids 2025 |
| Exposição e autonomia (IEA) por faixa: 9–10 · 11–12 · 13–14 · 15–17 | 29 · 44 · 57 · 60 | TIC Kids 2025 |
| Inclinação por ano de idade: IMR · IEA (descritivo, n = 4) | −4,6 p.p. · +4,8 p.p. | Notebook, Fase 4 |
| Pares de indicadores em que a exposição supera a mediação aos 15–17 anos | 9 de 9 | Notebook, Fase 5 |
| Faixa em que a exposição passa a superar a mediação (varia com o indicador) | 11–12 anos em 4 de 9 pares; de 9–10 a 15–17 nos demais | Notebook, Fase 5 |
| Responsáveis que usam recurso técnico para limitar o tempo na Internet | 37% | TIC Kids 2025 |
| Responsáveis que conversam sobre o que o filho faz online | 44% | TIC Kids 2025 |
| Aprendem sobre uso seguro com a própria criança ou adolescente | 50% | TIC Kids 2025 |
| **[SINTÉTICO]** Perfis de mediação (K-means, k = 6, silhueta 0,32) | IMR de 88 (perfil A) a 10 (perfil F) | Notebook, Fase 4 |
| **[SINTÉTICO]** Previsão do uso de recurso técnico (floresta aleatória) | AUC 0,66 no teste (IC95% 0,62 a 0,70) | Notebook, Fase 4 |
| **[SINTÉTICO]** Sensibilidade às suposições do gerador | AUC de 0,49 a 0,87 | Notebook, Fase 4 |

**Como ler os índices.** IMR é a média de três indicadores (pais colocam regras para o celular, olham o celular, deixam o filho sem o celular por um tempo). IEA é a média de três (usou IA generativa, pesquisou produtos para comprar, realizou compras). São escolhas de modelagem nossas, não medidas oficiais. Por isso fizemos a análise de sensibilidade com os 9 pares.

## Sobre os dados sintéticos

Não conseguimos os microdados do TIC Kids 2025, e a análise por registro precisa de pelo menos 1.000 linhas. Então o `scripts/criar_dados_sinteticos.py` gera **2.400 registros inventados** (600 por faixa etária) a partir dos percentuais públicos do TIC Kids. Alguns cuidados que tomamos:

- Nenhuma pessoa real é representada e não há dado pessoal nos arquivos (sem nome, escola, cidade ou contato).
- Os percentuais por faixa etária batem com os publicados (diferença de 0,00 p.p.). O que é suposição nossa é só a relação entre os indicadores, e testamos o que acontece quando ela muda.
- Os arquivos começam com `sintetico_`, existe a coluna `sintetico = True` e a página 4 do dashboard traz o aviso escrito.
- Esses dados não provam nada sobre famílias reais e não devem ser citados como resultado de pesquisa. Os detalhes estão em [`docs/ficha_dados_sinteticos.md`](docs/ficha_dados_sinteticos.md).

## Observações

- **Os critérios de sucesso de P1 e P2 não foram atingidos.** Deixamos isso no notebook como resultado, sem esconder. O critério de P2 não foi afrouxado depois de ver os dados. Os de P3 foram atingidos, mas em dados sintéticos e com a ressalva acima.
- **Denúncias medem reporte, não ocorrência.** A alta pode vir de mais crimes, de mais canais de denúncia ou dos dois. Não afirmamos causalidade.
- **n pequeno.** São 20 anos (P1) e 4 faixas etárias (P2). Os números de inclinação e de R² são só descritivos. Os dados sintéticos não resolvem isso, porque repetem os mesmos percentuais e não trazem conclusão nova sobre P1 ou P2.
- **Divergência entre edições da SaferNet:** a edição 2024 traz 25.166 (2011) e 17.443 (2015), e a de 2025 traz 25.116 e 17.433. Usamos a mais recente.
- **Linhas `leitura_grafico`:** parte dos valores do TIC Kids foi lida de gráficos e precisa ser conferida nas tabelas oficiais do Cetic.br antes da entrega.
- **Próximo passo:** com os microdados do TIC Kids 2025 dá para agrupar famílias por perfil de mediação (K-means) e prever quem não usa recurso técnico. Já testamos esse caminho com dados sintéticos (P3) e falta repetir com os dados reais.

## Estrutura

```
├── dados/                          tabelas em CSV (fonte e confiança em cada linha)
│   ├── safernet_*.csv, ticKids2025_*.csv     dados reais e agregados
│   └── sintetico_*.csv                       registros sintéticos (2.400) e a validação deles
├── docs/
│   └── ficha_dados_sinteticos.md   como geramos os dados sintéticos, limites e uso permitido
├── notebooks/
│   └── crispdm_controle_parental.ipynb   6 fases do CRISP-DM no formato do guia, já executado
├── dashboard/                      4 páginas em PNG (Pandas, Matplotlib, Seaborn). A 4ª é sintética
├── scripts/
│   ├── criar_dados.py              monta os CSVs reais
│   ├── criar_dados_sinteticos.py   gera os registros sintéticos
│   └── montar_notebook.py          gera o notebook
├── requirements.txt
└── README.md
```

## Como executar

**No Google Colab:** clique no botão "Abrir no Google Colab" no topo deste README e rode as células em ordem (Ambiente de execução > Executar tudo). A primeira célula baixa o repositório sozinha.

**No computador:**

```bash
pip install -r requirements.txt
python scripts/criar_dados.py
python scripts/criar_dados_sinteticos.py
jupyter nbconvert --to notebook --execute --inplace notebooks/crispdm_controle_parental.ipynb
```

## Fontes

- SAFERNET BRASIL. *Indicadores Denúncias 2025.* arquivos.safernet.org.br/pdfs/INDICADORES-DenunciasSaferNet2025.pdf
- CETIC.BR/NIC.BR. *TIC Kids Online Brasil 2025 – Principais Resultados.* 22 out. 2025. cetic.br/media/analises/tic_kids_online_brasil_2025_principais_resultados.pdf
- FUNDAÇÃO TELEFÔNICA VIVO. *Nota técnica: TIC Kids Online Brasil 2025.* 31 out. 2025.
- CHAPMAN, P. et al. *CRISP-DM 1.0: Step-by-step data mining guide.* 2000.
- VALÉRIA, K. *Guia Prático: o modelo CRISP-DM.* Ciência de Dados e Aprendizagem de Máquina, UDF (material da disciplina).
