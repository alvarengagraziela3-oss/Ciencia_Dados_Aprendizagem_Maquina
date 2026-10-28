<img src="assets/logo-udf.jpg" alt="UDF Centro Universitário" width="230">

**Profa. Kadidja Valéria | UDF**  
Ciência de Dados e Aprendizado de Máquina · Sistemas de Informação · 2026.2

# Aula 1 — Conceitos e classificação de problemas

## Identificação

- Estudante ou equipe: **Graziela Marcela Alvarenga Silva Viana**
- Turma: **PREENCHER**
- Data de realização: **27/10/2026**
- Integrantes e contribuições (se em equipe): **PREENCHER**

## Objetivos

Distinguir programação tradicional e Machine Learning, identificar atributos e alvo e diferenciar classificação, regressão e agrupamento.

## 1. Explicação com suas palavras

1. Como um modelo aprende com dados? **Ele aprende vendo exemplos. Você mostra vários e-mails já marcados como spam ou não spam, ele tenta adivinhar, confere se acertou e vai ajustando por dentro pra errar menos. Depois de muitas rodadas, ele pega os padrões e consegue classificar e-mails que nunca viu.**
2. Qual diferença entre algoritmo e modelo? **O algoritmo é o jeito de aprender, o passo a passo (árvore de decisão, regressão logística, rede neural). O modelo é o resultado depois que o algoritmo aprendeu com os dados: já treinado e pronto pra prever. O algoritmo é a receita, o modelo é o prato pronto.**
3. Compare uma regra de bloqueio de palavra com um modelo de spam. **A regra de bloqueio é simples: alguém escreve “se tiver ‘promoção’, bloqueia”. Dá pra entender fácil, mas é rígida. Bloqueia e-mail legítimo sem querer e o spammer escapa trocando uma letra (“pr0moção”).**
4. Dê um exemplo de atributo e alvo e defina o momento da previsão. **Atributos: remetente, quantidade de links, se tem palavras como “grátis” ou “urgente”, horário de envio.
Alvo: o e-mail é spam ou não.
Momento da previsão: quando o e-mail chega ao servidor, antes de cair na caixa de entrada. Só vale usar o que já se sabe nesse instante. Se o usuário marcar como spam depois, essa informação não pode entrar, senão o modelo “cola” e a previsão fica falsa (vazamento de dados).**

## 2. Quadro comparativo

| Critério | Supervisionado | Não supervisionado |
| --- | --- | --- |
| Presença de alvo no treino | Cada exemplo vem com a resposta certa | s dados vêm sem resposta pronta. |
| Pergunta que pode responder | “Esse e-mail é spam?” “Quanto vou vender semana que vem?” | “Que tipos de cliente existem?” “Tem algo estranho nessas operações?” |
| Tipo de saída | Uma categoria (spam/não spam) ou um número (valor em reais). | Grupos, padrões ou alertas de itens que fogem do normal. |
| Tarefas e exemplo | PREENCHER | PREENCHER |
| Dados necessários | PREENCHER | PREENCHER |
| Forma de avaliação | PREENCHER | PREENCHER |
| Limitação | PREENCHER | PREENCHER |

## 3. Situações-problema

Os casos são cenários didáticos. Escolha **pelo menos cinco** e justifique sua classificação pelo significado do alvo ou por sua ausência.

| Caso | Situação-problema |
| --- | --- |
| 1 Educação | Prever evadiu/permaneceu com histórico rotulado de turmas anteriores. |
| 2 Saúde | Estimar o tempo de espera em minutos a partir de registros de atendimento. |
| 3 Comércio | Descobrir perfis de compra sem categorias prévias de clientes. |
| 4 Finanças | Prever inadimplente/adimplente com contratos e desfechos conhecidos. |
| 5 Segurança digital | Distinguir spam/legítima com mensagens já revisadas. |
| 6 Comércio | Estimar o total de vendas em reais na próxima semana. |
| 7 Educação | Agrupar perfis de acesso ao ambiente virtual sem rótulo de evasão. |
| 8 Saúde | Classificar exames em categorias previamente definidas por especialistas. |

| Caso escolhido | Alvo ou ausência de alvo | Categoria, quantidade ou grupos? | Abordagem e justificativa | Dados necessários e limitação |
| --- | --- | --- | --- | --- |
| Educação | evadiu ou permaneceu, já rotulado nas turmas anteriores. | duas classes | Classificação supervisionada. O alvo é uma categoria conhecida e há histórico com a resposta certa para o modelo aprender. | Notas, frequência, acessos, perfil do aluno e o rótulo de evasão. Limitação: turmas antigas podem não representar as atuais, e pode haver poucos evadidos (classes desbalanceadas). |
| Saúde | tempo de espera em minutos. | valor numérico | Regressão supervisionada. O que se quer prever é um número, não uma classe. | Horário de chegada, dia da semana, tipo de atendimento, nº de profissionais, tempo real de espera. Limitação: imprevistos (emergências, picos) geram muito ruído e erro. |
| Comércio | não existem categorias | descobertos pelo modelo | Agrupamento (clustering), não supervisionado. Como não há resposta certa, o modelo só agrupa clientes parecidos. | Histórico de compras, frequência, valor gasto, tipos de produto. Limitação: não há “certo ou errado” para conferir, então alguém precisa interpretar e nomear os grupos. |
| Finança | inadimplente ou adimplente, com desfecho já conhecido nos contratos. | duas classes | Classificação supervisionada. O desfecho dos contratos antigos serve de resposta certa para o modelo aprender. | Renda, valor e prazo do contrato, histórico de pagamento, dados do cliente e o desfecho. Limitação: só temos o desfecho de quem recebeu crédito, então o modelo não conhece quem foi recusado (viés de seleção), e inadimplentes costumam ser minoria. |
| Segurança | spam ou legítima, já revisado por pessoas. | duas classes | Classificação supervisionada. As mensagens revisadas são o gabarito, e o modelo aprende os padrões de cada classe. | Texto da mensagem, remetente, links, horário e o rótulo da revisão. Limitação: spammers mudam de tática, então o modelo envelhece e precisa de retreino, e erros de revisão contaminam o aprendizado. |

## 4. Raciocínio crítico

“Detectar fraude” define sozinho o tipo de aprendizado? Compare o uso de exemplos rotulados e a busca de operações atípicas sem rótulos. **Não. Com exemplos rotulados: você já tem um histórico em que alguém marcou “isso foi fraude” e “isso foi normal”. O modelo aprende o que diferencia uma da outra e passa a reconhecer fraudes parecidas. É ótimo pra golpes que já conhecemos, mas costuma falhar com golpes novos, porque nunca viu algo igual. 
Sem rótulos: ninguém disse o que é fraude. O modelo só aprende como é o comportamento normal e avisa quando algo foge muito disso, tipo uma compra enorme, de madrugada, em outro país. Ajuda a achar golpes novos, mas nem tudo que é estranho é fraude (às vezes a pessoa só fez uma compra grande de verdade), então aparecem muitos alertas falsos e alguém precisa conferir.**

## Entrega

Salve este arquivo preenchido. Critérios: distinção conceitual, pertinência dos dados, justificativa e clareza. [Voltar ao início](README.md).
