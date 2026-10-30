# 1 Introdução
## 1.1 Finalidade
Este documento tem como objetivo apresentar uma visão da arquitetura de software do sistema Simplei Gerencial.
## 1.2 Escopo
O Simplei Gerencial é um sistema CLI de folha de pagamento.
## 1.3 Definições, Acrônimos e Abreviações
|Abreviação|Definição|
|---|---|
|CLI|Interface de Linha de Comando|
# 2 Representação da Arquitetura
O sistema terá como interface um CLI próprio. Através da entrada de usuário capturada por ele será adicionada a camada de negócio e por fim serão armazenadas as mudanças em um banco de dados Postgres.
## 2.1 Diagrama de Relações
[Diagrama de Relações.pdf](https://github.com/user-attachments/files/34204304/Diagrama.de.Relacoes.pdf)
## 3 Tecnologias
|Camada|Tecnologia|
|---|---|
|Entrada|Teclado|
|Front|Python, CLI|
|Back|Python|
|Banco de Dados|Postgres|
