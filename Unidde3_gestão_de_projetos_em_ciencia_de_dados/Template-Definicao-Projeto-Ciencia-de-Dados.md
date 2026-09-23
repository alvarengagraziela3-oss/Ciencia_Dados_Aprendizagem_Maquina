# Template - Definição do Projeto de Ciência de Dados

**Unidade:** III - Gestão de Projetos  
**Metodologia:** PBL + trabalho em equipes  
**Entregável:** Documento de definição do projeto

> **Finalidade:** delimitar um problema real e orientar o desenvolvimento do projeto de Ciência de Dados. Preencha todos os campos com informações objetivas, verificáveis e coerentes entre si.

## 1. Identificação do projeto

| Campo | Preenchimento |
|---|---|
| Título provisório do projeto |Ferramentas de controle parental: uma analise comparativa para a proteção infantojuvenil a luz da LGPD e ECA Digital |
| Curso / disciplina |Ciência de Dados e Aprendizagem de Máquina |
| Turma | |
| Equipe |Graziela Alvarenga - Gabriela Marcela |
| Integrantes e funções iniciais | |
| Professor(a) | Flávia Maria |
| Data de elaboração | |
| Versão do documento | |

## 2. Visão geral

### 2.1 Resumo do projeto

Em até 100 palavras, apresente o problema, o público-alvo, a proposta de análise e o resultado esperado.

**Preenchimento:**
crianças e adolescentes estão expostos a riscos cibernéticos (grooming, sextorsão, cyberbullying, sharenting) nas redes sociais, agravados pelo uso dual da IA, sem que as ferramentas de controle parental sejam auditadas tecnicamente.

### 2.2 Declaração do projeto em uma frase

Nosso projeto utilizará dados gerados em testes simulados de risco, somados à documentação técnica e às políticas de privacidade de cinco ferramentas de controle parental, para compreender a eficácia da detecção automatizada e o grau de transparência no tratamento de dados de menores, apoiando famílias, desenvolvedores e órgãos reguladores na decisão de qual ferramenta adotar e quais requisitos exigir de sistemas de proteção infantojuvenil.

________________________________________________________________________________

## 3. Contexto e definição do problema

### 3.1 Contexto

Descreva a situação atual, o ambiente em que o problema ocorre e as evidências iniciais que demonstram sua relevância.

- Onde o problema ocorre? 
- Quem é afetado? 
- Quais sinais, dados ou relatos indicam sua existência? 
- Por que é importante investigá-lo agora? 

**Preenchimento:**

Onde? Em redes sociais, aplicativos de mensagens, jogos e plataformas gamificadas acessadas por crianças e adolescentes;

Quem é afetado? Crianças e adolescentes de 9 a 17 anos, diretamente; pais e responsáveis, que assumem a mediação sem informação técnica suficiente

Sinais e dados que indicam a existência do problema: 93% das crianças e adolescentes brasileiros de 9 a 17 anos usam internet (cerca de 25 milhões), e 23% iniciaram o acesso antes dos 6 anos.
Cerca de 300 milhões de crianças e jovens no mundo sofreram algum tipo de crime cibernético em 12 meses, segundo relatório das Nações Unidas.
Estima-se que 19% do público de 12 a 17 anos já sofreu violência sexual facilitada por meios tecnológicos (UNICEF Innocenti, ECPAT, Interpol).
Parte expressiva das denúncias recebidas pela SaferNet envolve violações de direitos de crianças e adolescentes em ambientes digitais.

Por que investigar agora.? A entrada em vigor do ECA Digital (Lei nº 15.211/2025) cria obrigações novas de verificação de idade, supervisão parental e tratamento de dados de menores, mas não existe avaliação técnica independente que verifique se as ferramentas já disponíveis no mercado cumprem esses requisitos — nem se elas próprias respeitam a privacidade de quem dizem proteger.________________________________________________________________________________

________________________________________________________________________________

### 3.2 Problema central

Formule o problema de maneira específica, sem antecipar uma solução.

> **Modelo:** [Público/organização] enfrenta [problema observável] no contexto de [situação], produzindo [consequência ou impacto].

**Problema definido:** Pais e responsáveis enfrentam a ausência de informação técnica comparável e verificável sobre ferramentas de controle parental, no contexto da crescente exposição infantojuvenil a crimes cibernéticos potencializados por inteligência artificial, produzindo escolhas de proteção baseadas em marketing e não em evidência, com risco de adotar soluções ineficazes na detecção de conteúdo de risco ou excessivamente invasivas em relação aos dados do próprio menor.

________________________________________________________________________________

### 3.3 Evidências iniciais

| Evidência | Fonte | O que ela indica? | Confiabilidade / limitação |
|---|---|---|---|
| 1. 93% dos brasileiros de 9 a 17 anos usam internet; 23% começaram antes dos 6 anos  |Secretaria de Comunicação Social (2024)|Exposição precoce e praticamente universal, ampliando a superfície de risco |Alta (pesquisa oficial). Não mede incidentes, apenas acesso |
| 2.300 milhões de crianças e jovens vítimas de crime cibernético em 12 meses |ONU News (2024) |Dimensão global do problema |Alta credibilidade institucional; estimativa agregada, sem recorte Brasil |
| 3.19% do público de 12 a 17 anos sofreu violência sexual facilitada por tecnologia |UNICEF Innocenti / ECPAT / Interpol	 |Gravidade e prevalência dos crimes de natureza sexual online |Alta; metodologia de autorrelato pode gerar subnotificação |

## 4. Público-alvo e partes interessadas

### 4.1 Público-alvo principal

| Aspecto | Descrição |
|---|---|
| Quem são os usuários ou beneficiários? |Pais e responsáveis por crianças e adolescentes de 9 a 17 anos (usuários diretos do painel de controle) e os próprios menores monitorados (usuários do lado supervisionado). Secundariamente, desenvolvedores de software e órgãos reguladores |
| Quais necessidades possuem? |Proteger o menor sem depender de conhecimento técnico avançado; entender o que a ferramenta coleta e por que bloqueia; preservar a relação de confiança com o adolescente; cumprir o dever legal de cuidado |
| Como são afetados pelo problema? |Escolhem ferramentas sem base comparativa; podem confiar em soluções que falham na detecção de risco real ou que coletam dados sensíveis do menor além do necessário; adolescentes ficam sujeitos a decisões automatizadas sem explicação |
| Que decisão ou ação poderão tomar com os resultados? |Selecionar a ferramenta mais adequada ao seu contexto familiar, ajustar configurações de privacidade, e — no caso de desenvolvedores e reguladores — adotar ou exigir requisitos mínimos de transparência e minimização de dados |

### 4.2 Partes interessadas

| Parte interessada | Interesse no projeto | Influência | Forma de envolvimento |
|---|---|---|---|
|Famílias (pais e responsáveis) |Escolher proteção eficaz e não invasiva | Alta |Público-alvo dos resultados; validação da clareza do ranking |
|Crianças e adolescentes |Ser protegido sem vigilância arbitrária; direito à explicação | Média |Considerados como usuários na avaliação de IHC (interface do lado supervisionado) |
|Desenvolvedores de software |Requisitos claros de Privacy by Design e XAI | Média  |Destinatários do framework de requisitos proposto |
|Fornecedores das ferramentas| Reputação e conformidade legal| Alta | Objeto da auditoria; fonte de documentação pública|
| Escolas e educadores| Orientar famílias sobre segurança digital| Baixa | Difusão dos resultados|

## 5. Objetivos do projeto

### 5.1 Objetivo geral

Escreva um objetivo que indique o que será analisado, para qual finalidade e em qual contexto. Inicie com um verbo no infinitivo.

**Objetivo geral:**Analisar comparativamente as três ferramentas de controle parental quanto à qualidade, segurança, eficácia e recursos de IA, a partir de testes em cenários de risco simulados, pelas próprias autoras.

________________________________________________________________________________

### 5.2 Objetivos específicos

Defina de três a cinco objetivos mensuráveis e compatíveis com o prazo do projeto.

| Nº | Objetivo específico | Evidência de conclusão |
|---:|---|---|
| 1 |•	Mapear os principais riscos e o papel dual da IA |Capítulo com o conjunto de diretrizes, rastreável aos resultados da análise |
| 2 |•	Identificar os requisitos legais aplicáveis, definir critérios de avaliação baseados em IHC, XAI e privacidade desde a concepção |Matriz validada pela orientadora, com definição operacional de cada critério e da régua de pontuação |
| 3 |•	Comparar o desempenho das plataformas segundo esses critérios.  |Base documental estruturada, com data de coleta e extração das cláusulas relativas a coleta, retenção e compartilhamento de dados |
| 4 | | |
| 5 | | |

### 5.3 Verificação dos objetivos

Marque após revisar:

- [x] São específicos e escritos com clareza.
- [x] Podem ser verificados por meio de entregáveis ou métricas.
- [x] São viáveis com os dados, recursos e tempo disponíveis.
- [x] Estão diretamente relacionados ao problema central.
- [x] Consideram os usuários e a decisão que será apoiada.

## 6. Perguntas de negócio

As perguntas de negócio orientam a coleta, a análise e a comunicação dos resultados. Evite perguntas que possam ser respondidas apenas com “sim” ou “não”.

| Nº | Pergunta de negócio | Decisão apoiada | Dados necessários | Análise ou indicador possível |
|---:|---|---|---|---|
| 1 |Quais categorias de dados pessoais cada ferramenta coleta e por quanto tempo os retém, em relação ao estritamente necessário? |Avaliação de conformidade com a minimização prevista na LGPD |Políticas de privacidade, permissões solicitadas pelo app e configurações disponíveis |Índice de minimização: razão entre dados coletados e dados justificados pela finalidade declarada |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

## 7. Hipóteses iniciais

Registre suposições que serão investigadas, sem apresentá-las como conclusões.

| Hipótese | Como poderá ser testada? | Resultado que a refutaria? |
|---|---|---|
| H1.A interface do lado supervisionado (menor) oferece menos informação sobre o monitoramento do que a interface do responsável |Avaliação heurística comparada das duas interfaces, com o mesmo conjunto de heurísticas de Nielsen |Paridade informacional entre as duas interfaces |
| H2. | | |
| H3. | | |

## 8. Dados necessários e viabilidade

| Conjunto ou fonte de dados | Variáveis principais | Formato | Acesso / responsável | Qualidade esperada |
|---|---|---|---|---|
|Registros dos testes simulados de risco |ID do caso, categoria de risco, ferramenta, detecção (sim/não), tipo de alerta, tempo de resposta, texto exibido | |Gerado pela equipe; Graziela |Alta — dado primário, controlado pelo protocolo |
|Políticas de privacidade e termos de uso das cinco ferramentas |Categorias de dados coletados, base legal, prazo de retenção, compartilhamento com terceiros, mecanismos de exclusão | |Público; Gabriela |Média — textos extensos e sujeitos a atualização; exige registro da data de coleta |
|Capturas de tela das interfaces (pais e menor) |Tela, evento associado, presença de explicação, elementos de consentimento | |Gerado pela equipe |Alta — evidência direta, porém dependente da versão testada |

### 8.1 Avaliação inicial dos dados

- **Disponibilidade:** os dados primários dependem apenas da execução do protocolo pela equipe; os secundários são públicos e de acesso imediato.
- **Volume e período coberto:** estimados 5 ferramentas, cerca de 15 a 20 casos de teste. Registros primários, coletados entre outubro e novembro de 2026; documentação referente às versões vigentes no mesmo período.
- **Dados ausentes, duplicados ou inconsistentes previstos:** ausência de informação sobre técnicas de IA e prazos de retenção em parte dos fornecedores; possível divergência entre o que a política declara e o que o aplicativo solicita em permissões.
- **Necessidade de integração entre fontes:** 
- **Restrições legais, contratuais ou institucionais:** os termos de uso de algumas ferramentas restringem engenharia reversa e uso automatizado; a auditoria se limita à observação de comportamento na interface, sem interceptação de tráfego ou descompilação.

### 8.2 Privacidade, ética e segurança

- [x] A equipe verificou se há dados pessoais ou sensíveis.
- [x] A coleta e o uso dos dados possuem finalidade legítima e explícita.
- [x] O acesso será limitado às pessoas autorizadas.
- [x] Dados pessoais serão minimizados, anonimizados ou pseudonimizados quando necessário.
- [x] Possíveis vieses e impactos sobre grupos serão analisados.
- [x] A divulgação dos resultados evitará reidentificação ou exposição indevida.

**Cuidados específicos deste projeto:** Nenhuma criança ou adolescente real participa dos testes: os cenários de risco são simulados em contas e dispositivos de teste criados pela própria equipe, com perfis fictícios. Não há coleta de conversas reais, prints de terceiros ou dados de usuários das plataformas. O conteúdo textual usado nos testes é construído pela equipe a partir de tipologias descritas na literatura, sem reproduzir material de abuso. As capturas de tela publicadas no trabalho serão tratadas para remover identificadores de conta. Os resultados serão apresentados como avaliação técnica de produtos, com data e versão registradas, evitando afirmações difamatórias sobre fornecedores.

________________________________________________________________________________

## 9. Escopo do projeto

| Dentro do escopo | Fora do escopo |
|---|---|
|Cinco ferramentas: Google Family Link, Qustodio, Kaspersky Safe Kids, Microsoft Family Safety e KidsControl |Desenvolvimento ou treinamento de modelo próprio de PLN/ML|
|Testes simulados de detecção em ambiente controlado |Pesquisa com participantes humanos, crianças ou adolescentes reais |
|Verificação de aderência à LGPD (com ênfase no art. 14) e ao ECA Digital |Análise de custo-benefício comercial ou recomendação de compra |
|Análise documental de políticas de privacidade e permissões |Avaliação jurídica conclusiva ou parecer legal |

**Restrições conhecidas:** Prazo curto (setembro a novembro de 2026, conforme cronograma da orientação); versões gratuitas ou de teste das ferramentas podem limitar funcionalidades avaliáveis; ausência de APIs públicas de classificação impede medição direta de acurácia dos modelos, restringindo a análise ao comportamento observável na interface; equipe de duas integrantes conciliando outras disciplinas.

________________________________________________________________________________

## 10. Resultados e entregáveis previstos

| Entregável | Descrição | Formato | Responsável | Critério de aceite |
|---|---|---|---|---|
| Base tratada |Registros dos testes, codificação das interfaces e extração das políticas, unificados por ferramenta e critério | |Equipe |Sem registros duplicados; todos os casos de teste com resultado preenchido e evidência associada |
| Análise exploratória | | | | |
| Visualizações / painel |Pontuação de cada ferramenta nos critérios das três dimensões, com justificativa e evidência por célula |tabela no TCC |Equipe |	Cada pontuação rastreável a uma evidência registrada |
| Relatório ou apresentação |Artigo |Documento |Equipe |Aderente às normas ABNT e ao cronograma da orientação |
| Outro | | | | |

## 11. Critérios de sucesso

Defina como a equipe saberá se o projeto alcançou seus objetivos.

| Critério | Indicador ou evidência | Meta | Forma de verificação |
|---|---|---|---|
| Relevância para o problema |Perguntas de negócio respondidas com evidência |5 de 5 |Conferência entre a seção 6 e o capítulo de resultados |
| Qualidade dos dados |Casos de teste executados e registrados com evidência |95% dos casos previstos |Auditoria da base tratada |
| Qualidade da análise |Células da matriz com justificativa rastreável |100% |Revisão cruzada entre as integrantes e validação da orientadora |
| Utilidade para o público-alvo |Ranking compreensível por leitor sem formação técnica | |Leitura-teste informal antes da entrega final |
| Comunicação dos resultados |Apresentação entregue |Sem pendências |Validação da orientadora e da banca |

## 12. Plano inicial de trabalho

| Etapa | Atividades principais | Responsável(is) | Prazo | Dependências |
|---|---|---|---|---|
| 1. Definição |Ajuste do título e do problema, revisão do referencial (crimes cibernéticos, IA, marco regulatório, IHC) |Equipe |Setembro/2026 | |
| 2. Obtenção dos dados |Seleção final das ferramentas, criação das contas de teste, coleta das políticas e permissõe | |Outubro/2026 |Etapa 1 e definição sobre versões pagas |
| 3. Preparação dos dados |Construção da matriz multicritério, do protocolo de testes e da planilha de codificação |Equipe |Outubro/2026 |Etapa 2 |
| 4. Análise / modelagem |Execução dos testes simulados, pontuação da matriz, análise exploratória e visualizações |Equipe |Outubro–Novembro/2026 |Etapa 3 |
| 5. Validação |Revisão cruzada das pontuações, verificação das hipóteses, validação com a orientadora |Equipe e Flávia |Novembro/2026 |Etapa 4 |
| 6. Comunicação |Redação do ranking e do framework, conclusão, revisão ABNT e apresentação |Equipe |Novembro–Dezembro/2026 |Etapa 5 |

## 13. Riscos do projeto

| Risco | Probabilidade | Impacto | Estratégia de resposta | Responsável |
|---|---|---|---|---|
|Funcionalidades essenciais indisponíveis na versão gratuita das ferramentas	 | Alta |  Alto |Definir antecipadamente quais critérios exigem versão paga; usar períodos de teste gratuito e registrar a versão avaliada | |
|Documentação técnica insuficiente sobre as técnicas de IA empregadas | Alta | Médio |Tratar a opacidade como resultado da auditoria, pontuando-a no critério de transparência |Equipe |
|Atraso pelo acúmulo com outras disciplinas |  Baixo |  Médio  |Reuniões semanais de acompanhamento aos sábados; entregas parciais por capítulo |Equipe e Flávia |

## 14. Organização da equipe

| Integrante | Papel principal | Responsabilidades | Apoio necessário |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |

## 15. Validação da definição do projeto

Antes da entrega, confirme:

- [x] O problema é real, relevante e delimitado.
- [x] O público-alvo e as partes interessadas estão identificados.
- [x] O objetivo geral e os objetivos específicos são coerentes.
- [x] As perguntas de negócio orientam decisões concretas.
- [x] Há dados potencialmente disponíveis para responder às perguntas.
- [x] O escopo é compatível com o prazo e os recursos.
- [x] Os critérios de sucesso são mensuráveis.
- [x] Riscos, privacidade, ética e segurança foram considerados.
- [x] Funções e responsabilidades foram distribuídas.

## 16. Aprovação e registro de ajustes

| Responsável | Validação / observação | Data |
|---|---|---|
| Representante da equipe: Gabriela|[preencher após revisão da equipe] | |
| Professor(a) / orientador(a): Flávia |[preencher após apresentação inicial] | |

### Ajustes solicitados após a apresentação inicial

________________________________________________________________________________

________________________________________________________________________________

