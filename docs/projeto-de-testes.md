# SimGer - Simplei Gerencial

# 1 Introdução
## 1.1 Propósito do documento
O propósito desse documento é de descrever os projetos de teste. Simplei é um sistema de folha de pagamento de cli.
## 1.2 Siglas, Acrônimos e Descrições
|Termo|Descrição|
|---|---|
|Branch|Ramo isolado de desenvolvimento|
|UAT|Teste de Aceitação do Usuário|
# 2 Estratégias de Testes
## 2.1 Estratégias
### 2.1.1 Testes Unitários
Testa a menor unidade do software (função, método, classe) de forma isolada.
Será utilizado o framework pytest. Com combertura de 90%.
### 2.1.2 Testes de Integração
Testa a integração entre componentes e módulos.
Será utilizado a estratégia Top-Down com pytest.
### 2.1.3 Testes de Sistema
Testa o sistema completo como um todo, do início ao fim.
Esses testes serão feitos pela equipe de QA.
### 2.1.4 Teste de Aceitação
Testa se o sistema atende às necessidades do cliente/usuário.
Será utilizado um teste UAT com o sistema.
## 2.2 Técnicas de Teste
Serão utilizados testes automatizados com pytest e testcontainers, bem como testes manuais.
# 2 Recursos
## 3.1 Ambiente de testes
O ambiente de testes será uma branch própria no github do projeto, apenas será necessário o git instalado para realizar os testes.
