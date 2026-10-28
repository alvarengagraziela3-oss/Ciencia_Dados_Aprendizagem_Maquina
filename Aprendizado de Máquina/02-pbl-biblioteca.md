<img src="assets/logo-udf.jpg" alt="UDF Centro Universitário" width="230">

**Profa. Kadidja Valéria | UDF**  
Ciência de Dados e Aprendizado de Máquina · Sistemas de Informação · 2026.2

# PBL — Biblioteca em Foco

## Identificação

- Estudante ou equipe: **Graziela Marcela Alvarenga Silva Viana**
- Turma: **PREENCHER**
- Data de realização: **21/10/2026**
- Integrantes e contribuições (se em equipe): **PREENCHER**

## Situação-problema

Uma biblioteca universitária enfrenta filas em horários específicos e baixa utilização de alguns serviços. A coordenação deseja melhorar o atendimento e planejar recursos. Este é um cenário didático.

**Público-alvo:** estudantes usuários, equipe de atendimento e gestão.

**Questão norteadora:** como os dados podem orientar o planejamento da biblioteca e a oferta de serviços sem identificar ou discriminar seus usuários?

## Investigação em equipe

1. Delimitem o problema e a decisão a apoiar.
2. Registrem o que já sabem e o que precisam investigar.
3. Formulem duas perguntas de negócio.
4. Definam a unidade de análise, os atributos e o alvo, quando houver.
5. Justifiquem a abordagem e indiquem se uma análise descritiva já seria suficiente.
6. Proponham avaliação, cuidados com os dados e limitações.

## Canvas da equipe

| Campo | Registro |
| --- | --- |
| Problema e decisão | A biblioteca tem fila em alguns horários e serviços que quase ninguém usa. Precisamos decidir quantos atendentes colocar em cada horário e o que fazer com os serviços parados. |
| Público-alvo | Estudantes, equipe de atendimento e gestão. |
| O que sabemos | Tem fila em certos horários e alguns serviços são pouco usados. Mas não sabemos quais horários, quais serviços, nem o motivo. |
| O que precisamos investigar | Quando a fila aparece, se piora em época de prova ou começo de semestre, e se os serviços parados são pouco usados por falta de divulgação ou de interesse. |
| Pergunta de negócio 1 | Em quais dias e horários a fila é maior e quantos atendentes precisamos em cada um? |
| Pergunta de negócio 2 | Quais serviços são pouco usados e como as pessoas costumam usar a biblioteca? |
| Unidade de análise e período | Pergunta 1: cada hora de cada dia. Pergunta 2: cada serviço por semana. Período: um semestre inteiro. |
| Atributos, unidades e origem pretendida | Dia da semana, hora, época do semestre, quantas pessoas entram por hora (catraca), quantos atendentes estão no balcão, quantos empréstimos por hora e quantas vezes cada serviço foi usado por semana. Os dados vêm da catraca, do sistema de empréstimo e da escala da equipe. |
| Alvo e momento em que será conhecido, ou ausência de alvo | Pergunta 1: o alvo é o tempo de espera em minutos, que só sabemos no fim de cada hora. Por isso, na hora de prever, usamos só o que já se sabe antes (dia, horário, calendário, escala). Pergunta 2: sem alvo, porque ninguém definiu grupos de serviço ou de usuário antes. |
| Abordagem e justificativa | Primeiro olhar os números de forma simples. Se der pra prever a espera, usar regressão. Para entender o uso dos serviços, agrupar os parecidos, já que não há resposta pronta. |
| Alternativa sem ML | Uma tabela com médias por dia e hora, um ranking dos serviços mais e menos usados e uma conversa com a equipe. Provavelmente já resolve a escala. |
| Como avaliar a proposta | Ver se a previsão erra menos que a média simples, testando em um período que o modelo não viu. Na prática, ver se a fila diminuiu nos horários de pico depois de mudar a escala. |
| Privacidade e limitações | Usar só contagens, sem identificar ninguém, seguindo a LGPD. Não usar curso, gênero ou outras características pessoais pra decidir quem recebe melhor atendimento. Limitações: um semestre pode não valer pro próximo, e greve ou reforma bagunçam os dados. |

## Registro de colaboração

| Integrante | Papel | Contribuição |
| --- | --- | --- |
| Graziela Marcela Alvarenga Silva Viana | Todo o trabalho | Em todo o trabalho |

## Conclusão da equipe

**Proposta:** começar olhando os dados simples de catraca, empréstimos e escala pra achar os horários de pico e os serviços parados. Se isso não bastar, usar um modelo pra prever a espera e agrupar os serviços, sempre sem identificar ninguém.

**Dúvida ainda aberta:** será que existem dados de catraca e atendimento hora a hora, de um semestre inteiro?

**Feedback recebido e melhoria realizada:** PREENCHER

## Entrega

Canvas preenchido e síntese para apresentação de dois minutos. Avaliar coerência da pergunta, dados, abordagem, responsabilidade e colaboração. [Voltar ao início](README.md).
