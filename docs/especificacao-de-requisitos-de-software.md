# 1 Introdução
## 1.1 Objetivo
Este documento especifica os requisitos do Simplei Gerencial, fornecendo aos desenvolvedores as informações necessárias
para o projeto e implementação, assim como para a realização dos testes e homologação do sistema.
## 1.2 Escopo
Este documento descreve os requisitos funcionais e não-funcionais relacionados ao projeto Simplei Gerencial.
## 1.3 Definições e Siglas
* CLI - Interface de Linha de Comando. Meio pelo qual um programa pode ser executado em um prompt de comando.
* IDE - Ambiente de Desenvolvimento Integrado. Software utilizado para escrever e depurar código.
* PIP - Instalador de Pacotes Pip. Gerenciador padrão de bibliotecas Python
* Classe - Molde para criar objetos em Python.
* Git - Sistema de controle de versão.
# 2 Descrição do Sistema
Um sistema de folha de pagamento que permite o cadastro, gerenciamento e cálculo dos salários de colaboradores de diferentes categorias, gerando relatórios individuais e consolidados da folha de pagamento.
# 3 Requisitos Funcionais
## 3.1 [RF001] Cadastro de Administradores
O sistema deverá permitir o cadastro de administradores de domínio com e-mail e senha.
## 3.2 [RF002] Cadastro de Usuário
O sistema deverá permitir o cadastro de novos usuário em um domínio.
## 3.3 [RF003] Consulta de Usuários
O sistema deverá permitir a busca de usuários cadastrados contendo seus dados cadastrais.
## 3.4 [RF004] Manutenção de Usuários
O sistema deverá permitir: Inclusão de novos usuários, Alteração de usuários existentes, Exclusão de usuários e Consulta de usuários.
## 3.5 [RF005] Cadastro de Colaborador
O sistema deverá permitir o cadastro de colaboradores contendo: Matrícula, Nome, Salário Base e Tipo de Colaborador
## 3.6 [RF006] Cadastro de Colaborador Padrão
O sistema deverá permitir cadastrar colaboradores que recebem apenas salário base.
## 3.7 [RF007] Cadastro de Colaborador Comissionado
O sistema deverá permitir informar Valor das vendas e Percentual de comissão para cálculo posterior da remuneração.
## 3.8 [RF008] Cadastro de Colaborador por Produção
O sistema deverá permitir informar Quantidade produzida e Valor pago por unidade produzida para cálculo posterior da remuneração.
## 3.9 [RF009] Consulta de Colaboradores
O sistema deverá apresentar a lista de colaboradores cadastrados contendo seus dados cadastrais e remuneratórios.
## 3.10 [RF010] Cálculo de Salário
O sistema deverá calcular automaticamente o salário final de cada colaborador de acordo com sua categoria de remuneração.
## 3.11 [RF011] Geração da Folha de Pagamento
O sistema deverá gerar uma folha contendo: Matrícula, Nome, Tipo de colaborador e Valor do salário final para todos os colaboradores cadastrados.
## 3.12 [RF012] Emissão de Resumo da Folha
O sistema deverá apresentar o valor total da folha de pagamento somando o salário final de todos os colaboradores.
## 3.13 [RF013] Manutenção de Cadastros
O sistema deverá permitir: Inclusão de colaboradores, Alteração de colaboradores, Exclusão de colaboradores, Consulta de colaboradores.
## 3.14 [RF014] Exclusão de Domínio
O sistema deverá permitir a exclusão de domínio pelo administrador bem como todos os cadastros dos usuários, colaboradores e administrador.
# 4 Regras de Negócio
## 4.1 [RN001] Matrícula Única
Toda matrícula deverá ser única dentro do sistema.
## 4.2 [RN002] Nome Obrigatório
O nome do colaborador é obrigatório.
## 4.3 [RN003] Salário Não Negativo
O salário base não poderá ser negativo.
## 4.4 [RN004] Venda Não Negativa
O valor de vendas não poderá ser negativo.
## 4.5 [RN005] Comissão Não Negativo
O percentual de comissão não poderá ser negativo.
## 4.6 [RN006] Produção Não Negativa
A quantidade produzida não poderá ser negativa.
## 4.7 [RN007] Unidade Produzida Não Negativa
O valor pago por unidade produzida não poderá ser negativo.
## 4.8 [RN008] Cálculo de Salário Automático
O salário final deverá ser calculado automaticamente pelo sistema.
# 5 Requisitos Não Funcionais
## 5.1 [RNF001] Entrada do Sistema
O sistema deve ser utilizável através de entrada de teclado.
## 5.2 [RNF002] Filtro de Entrada
O sistema deve garantir apenas entradas de dados válidas.
## 5.3 [RNF003] Facilidade de Uso
Novos usuários devem conseguir cadastrar usuários e colaboradores, bem como emitir relatórios sem a ajuda de tutorias.
## 5.4 [RNF004] Disponibilidade
O sistema deve estar disponível em pelo menos 95% do tempo de uso.
## 5.5 [RNF005] Tempo de Resposta
O sistema deve ter tempo de resposta de até 2 Segundos.
## 5.6 [RNF006] Criptografia
O sistema deve cripografar senhas de usuários.
## 5.7 [RNF007] Autorização
O sistema deve pedir usuário e senha para acesso.
## 5.8 [RNF008] Acesso
O sistema deve checar o acesso a funcionalidades por usuário.
## 5.9 [RNF009] Auditoria
O sistema deve registrar todas a ações e mudanças feitas e salvá-las para acesso posterior pelo administrador.
# 6 Critérios de Aceitação
## 6.1 Requisitos Funcionais
| Requisito Funcional | Critérios Aprovadores |
|-----------------|----------------------|
| RF001 | Administrador consegue cadastrar-se com e-mail válido e senha; sistema rejeita e-mails duplicados, formatos inválidos e senhas com menos de 8 caracteres; confirmação exibida após cadastro bem-sucedido |
| RF002 | Administrador consegue cadastrar novo usuário no domínio informando nome, e-mail e senha; sistema valida unicidade de e-mail no domínio, formato de e-mail e força de senha; usuário aparece na lista de usuários do domínio |
| RF003 | Administrador consegue buscar usuários por nome ou e-mail; resultados exibem nome, e-mail, data de cadastro e status; busca retorna vazio quando nenhum usuário corresponde; paginação funciona para mais de 20 resultados |
| RF004 | Administrador consegue incluir, alterar (nome, e-mail, status), excluir e consultar usuários; exclusão exige confirmação; alteração de e-mail valida unicidade; usuários excluídos não aparecem nas consultas |
| RF005 | Administrador consegue cadastrar colaborador informando matrícula única, nome obrigatório, salário base não negativo e tipo (Padrão, Comissionado, Produção); sistema valida todos os campos obrigatórios e regras de negócio; colaborador aparece na lista |
| RF006 | Para colaborador Padrão, sistema aceita apenas matrícula, nome e salário base; cálculo de salário final igual ao salário base; não permite informar vendas, comissão, produção ou valor unitário |
| RF007 | Para colaborador Comissionado, sistema aceita valor de vendas não negativo e percentual de comissão não negativo; cálculo: salário base + (vendas × comissão%); validações impedem valores negativos |
| RF008 | Para colaborador Produção, sistema aceita quantidade produzida não negativa e valor por unidade não negativo; cálculo: salário base + (quantidade × valor unidade); validações impedem valores negativos |
| RF009 | Lista de colaboradores exibe matrícula, nome, tipo, salário base, dados específicos do tipo (vendas/comissão ou produção/valor unitário) e salário final calculado; ordenação por nome ou matrícula; filtro por tipo |
| RF010 | Sistema calcula salário final automaticamente ao cadastrar/alterar colaborador: Padrão = base; Comissionado = base + (vendas × comissão%); Produção = base + (quantidade × valor unidade); recálculo ocorre ao alterar qualquer campo remuneratório |
| RF011 | Folha de pagamento gera relatório com matrícula, nome, tipo de colaborador e salário final de todos os colaboradores ativos; totalizador no rodapé; opção de exportar para PDF/CSV; data de geração registrada |
| RF012 | Resumo da folha exibe valor total da folha (soma dos salários finais de todos colaboradores); valor atualiza automaticamente ao alterar cadastros; formato monetário brasileiro (R$ 1.234,56) |
| RF013 | Administrador consegue incluir, alterar (todos os campos exceto matrícula), excluir e consultar colaboradores; exclusão exige confirmação e remove da folha; alteração de tipo recalcula salário; matrícula imutável após criação |
| RF014 | Administrador consegue excluir domínio; exclusão remove todos os usuários, colaboradores e o próprio administrador; exige confirmação dupla; ação irreversível; domínio excluído não acessível |
## 6.2 Regras de Negócio
| RN001 | Sistema impede cadastro de colaborador com matrícula já existente; mensagem de erro clara: "Matrícula já cadastrada"; validação ocorre antes de salvar |
| RN002 | Sistema impede cadastro de colaborador sem nome; campo nome obrigatório; mensagem: "Nome é obrigatório"; validação em tempo real e ao submeter |
| RN003 | Sistema impede salário base negativo; aceita zero e valores positivos; mensagem: "Salário base não pode ser negativo"; validação para todos os tipos de colaborador |
| RN004 | Para colaborador Comissionado, sistema impede valor de vendas negativo; aceita zero; mensagem: "Valor de vendas não pode ser negativo" |
| RN005 | Para colaborador Comissionado, sistema impede percentual de comissão negativo; aceita zero; mensagem: "Percentual de comissão não pode ser negativo" |
| RN006 | Para colaborador Produção, sistema impede quantidade produzida negativa; aceita zero; mensagem: "Quantidade produzida não pode ser negativa" |
| RN007 | Para colaborador Produção, sistema impede valor por unidade negativo; aceita zero; mensagem: "Valor por unidade não pode ser negativo" |
| RN008 | Salário final sempre calculado automaticamente pelo sistema; não há campo manual para salário final; alteração em qualquer variável remuneratória dispara recálculo imediato |
## 6.3 Requisitos Não Funcionais
| RNF001 | Todas as funcionalidades acessíveis via teclado (Tab, Enter, setas); ordem de foco lógica; nenhum elemento requer mouse obrigatoriamente |
| RNF002 | Sistema valida todas as entradas: e-mails, números, datas, campos obrigatórios; mensagens de erro claras e específicas; entrada inválida não salva e mantém foco no campo |
| RNF003 | Fluxos principais (cadastrar usuário, cadastrar colaborador, emitir folha) concluídos por usuário novato em até 5 minutos sem documentação; interfaces autoexplicativas com labels e placeholders |
| RNF004 | Sistema disponível 95% do tempo em janela de 30 dias; downtime planejado comunicado com 48h antecedência; monitoramento de uptime ativo |
| RNF005 | Tempo de resposta ≤ 2 segundos para 95% das requisições (listagens, cadastros, cálculos, relatórios); medido em ambiente de homologação com carga simulada |
| RNF006 | Senhas armazenadas com hash bcrypt (cost ≥ 12); nunca em texto plano; logs não expõem senhas; reset de senha usa token temporário expiravel |
| RNF007 | Acesso ao sistema exige autenticação (usuário + senha); sessão expira após 30 min de inatividade; máximo 5 tentativas falhas bloqueia conta por 15 min |
| RNF008 | Sistema verifica permissão por funcionalidade: admin acessa tudo; usuário comum apenas consulta; ações restritas retornam 403; matrix de permissões documentada |
| RNF009 | Todas as ações (CRUD usuários, colaboradores, domínios, emissão relatórios, login/logout) registradas em log de auditoria com: usuário, ação, timestamp, entidade afetada, valores antes/depois; logs imutáveis e acessíveis apenas a admin |
