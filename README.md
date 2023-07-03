# Base de Horas - Ivy

Em meu estágio atual, eu tive um grande problema de ultrapassar o limite de horas por conta da alta demanda na empresa. Com este contexto e utilizando meus conhecimentos com Python, criei uma ferramenta para que as pessoas possam ter um controle sobre suas horas tanto no ambiente corporativo ou mesmo para uso pessoal, como controlar as horas de estudos, tempo de viagem, etc. 

O projeto recebe por mim, o apelido de Ivy, já que é meu primeiro projeto que venho a realizar por conta própria e consequentemente, meu primeiro animal de estimação que eu tive o interesse para ter foi minha gata chamada Ivy. E por gostar muito dela e gostar de muitos animais, considerei dar o nome do projeto com o nome dela.

## Como Utilizar:

A ferramenta tem o objetivo de ser prática e funcional, por isso, ela realiza as funções de CRUD. Ou seja, é capaz de inserir, visualizar, alterar e deletar dados:

### Inserindo Dados:

A primeira etapa é a inserção da data que o usuário queira inserir, a inserção consiste em selecionar uma data a partir de um mês e ano no calendário e clicar em cima do dia que queira adicionar no campo.

Após está etapa, deve-se preencher o campo "Horário de Entrada" e "Horário de Saida" com as respectivas horas de inicio e fim. Por conta de haver diversas formas de formato de hora, o campo é livre para inserir a forma que mais satisfazer o usuário.

Além disso, é possível inserir alguma informação extra no campo "Observações" a respeito dos valores.

Por fim, basta clicar no botão "Inserir" que automáticamente, os campos preenchidos serão 'apagados' e os dados estarão salvos em uma base de dados.

### Visualizando Dados:

É possível visualizar sua base de horas na tabela que encontra-se no campo direito. Nela, é possível visualizar o ID, a data, os horários de entrada e saída e as observações inseridas. Nesta tabela, é possível selecionar um valor e também, ajustar o dimensionamento da(s) coluna(s).

### Alterando Dados:

Caso o usuário queira alterar algum valor de algum registro na tabela, basta selecionar na tabela e clicar no campo "Atualizar" que você poderá alterar os campos que achar necessário. Feita as alterações, basta clicar no botão "Confirmar" que os novos dados irão ser atualizados na tabela e no banco de dados.

### Deletando Dados:

Caso o usuário queira deletar algum valor de algum registro na tabela, basta selecionar na tabela e clicar no campo "Deletar" que será excluido o valor tanto da tabela quanto do banco de dados.

## Tecnologias Utilizadas:

Neste projeto, foram usados as seguintes tecnologias e ferramentas:

- Python;
- Tkinter;
- SQlite;

## Limitações:

- A ferramenta não realiza cálculos automáticos das horas trabalhadas ou estudadas.
- A ferramenta não possui integração com outras plataformas ou serviços.
- A ferramenta armazena os dados localmente no dispositivo do usuário.