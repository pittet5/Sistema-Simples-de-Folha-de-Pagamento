# 1 Introdução
Este documento tem como objetivo listar os casos de uso do sistema. 

# 2 Diagrama de Caso de Uso

# 3 Especificação dos casos de uso

## UC01: Cadastrar Administrador
|**Objetivo:**| Permite que um administrador de domínio cadastre-se no sistema com e-mail e senha.|
|---|---|
|**Requisitos:**| RF001|
|**Atores:**| Administrador|
|**Prioridade:**| Alta|
|**Pré-condições:**| Nenhum administrador cadastrado para o domínio.|
|**Frequência de uso:**| Baixa (ocorre uma vez por domínio)|
|**Criticalidade:**| Alta|
|**Condição de Entrada:**| Administrador acessa a tela de cadastro e clica em "Cadastrar Administrador".|
|**Fluxo Principal:**|1. O administrador acessa a tela de cadastro de administrador;<br>2. O administrador informa e-mail válido e senha com mínimo 8 caracteres;<br>3. O sistema valida formato de e-mail, unicidade do e-mail e força da senha;<br>4. O sistema criptografa a senha com bcrypt (cost ≥ 12);<br>5. O sistema registra o administrador no domínio;<br>6. O sistema exibe mensagem de confirmação de cadastro bem-sucedido;<br>7. Caso de uso encerrado.|
|**Fluxo Alternativo:**|1a. E-mail já cadastrado: Sistema exibe erro "E-mail já cadastrado" e mantém foco no campo;<br>1b. Formato de e-mail inválido: Sistema exibe erro "Formato de e-mail inválido";<br>1c. Senha com menos de 8 caracteres: Sistema exibe erro "Senha deve ter no mínimo 8 caracteres".|
|**Pós-condições:**| Administrador cadastrado e autenticado no sistema.|
|**Regras de negócio:**| RN001 (unicidade de e-mail), RNF006 (criptografia de senha).|

## UC02: Login no Sistema
**Objetivo:** Permite que usuários e administradores acessem o sistema através de autenticação.
**Requisitos:** RNF007, RNF008
**Atores:** Administrador, Usuário
**Prioridade:** Alta
**Pré-condições:** Usuário cadastrado no sistema.
**Frequência de uso:** Muito alta (cada acesso ao sistema)
**Criticalidade:** Alta
**Condição de Entrada:** Usuário informa credenciais na tela de login e clica em "Entrar".
**Fluxo Principal:**
1. O usuário acessa a tela de login;
2. O usuário informa e-mail e senha;
3. O sistema valida as credenciais contra o hash armazenado;
4. O sistema verifica se a conta não está bloqueada (máx. 5 tentativas falhas);
5. O sistema cria sessão com expiração de 30 minutos de inatividade;
6. O sistema redireciona para a dashboard conforme perfil de acesso;
7. Caso de uso encerrado.
**Fluxo Alternativo:**
1a. Credenciais inválidas: Sistema exibe erro "E-mail ou senha incorretos"; após 5 tentativas, bloqueia conta por 15 minutos;
1b. Conta inativa: Sistema exibe erro "Conta desativada, contate o administrador".
**Pós-condições:** Usuário autenticado com sessão ativa.
**Regras de negócio:** RNF007 (autenticação obrigatória), RNF008 (verificação de permissões).

## UC03: Cadastrar Usuário
**Objetivo:** Permite que o administrador cadastre novos usuários em seu domínio.
**Requisitos:** RF002
**Atores:** Administrador
**Prioridade:** Alta
**Pré-condições:** Administrador logado no sistema.
**Frequência de uso:** Média
**Criticalidade:** Média
**Condição de Entrada:** Administrador acessa menu "Usuários" e clica em "Novo Usuário".
**Fluxo Principal:**
1. O administrador acessa a tela de cadastro de usuário;
2. O administrador informa nome, e-mail e senha do novo usuário;
3. O sistema valida unicidade de e-mail no domínio, formato de e-mail e força de senha;
4. O sistema criptografa a senha com bcrypt;
5. O sistema registra o usuário no domínio com status "Ativo";
6. O sistema exibe o usuário na lista de usuários do domínio;
7. Caso de uso encerrado.
**Fluxo Alternativo:**
1a. E-mail duplicado no domínio: Sistema exibe "E-mail já cadastrado neste domínio";
1b. Formato de e-mail inválido: Sistema exibe "Formato de e-mail inválido";
1c. Senha fraca: Sistema exibe requisitos de senha.
**Pós-condições:** Usuário cadastrado e disponível para login.
**Regras de negócio:** RF002 validações, RNF006 (criptografia).

## UC04: Consultar Usuários
**Objetivo:** Permite que o administrador busque e visualize usuários cadastrados no domínio.
**Requisitos:** RF003
**Atores:** Administrador
**Prioridade:** Média
**Pré-condições:** Administrador logado; usuários cadastrados.
**Frequência de uso:** Alta
**Criticalidade:** Baixa
**Condição de Entrada:** Administrador acessa menu "Usuários" > "Consultar".
**Fluxo Principal:**
1. O administrador acessa a tela de consulta de usuários;
2. O sistema exibe lista paginada (20 por página) com nome, e-mail, data de cadastro e status;
3. O administrador pode filtrar por nome ou e-mail;
4. O administrador pode ordenar por nome, e-mail ou data;
5. Caso de uso encerrado.
**Fluxo Alternativo:**
1a. Nenhum usuário cadastrado: Sistema exibe mensagem "Nenhum usuário encontrado";
1b. Busca sem resultados: Sistema exibe "Nenhum usuário corresponde à busca".
**Pós-condições:** Lista de usuários exibida.
**Regras de negócio:** Paginação para >20 resultados (RF003).

## UC05: Alterar Usuário
**Objetivo:** Permite que o administrador altere dados de usuários existentes.
**Requisitos:** RF004
**Atores:** Administrador
**Prioridade:** Média
**Pré-condições:** Administrador logado; usuário alvo existe.
**Frequência de uso:** Média
**Criticalidade:** Média
**Condição de Entrada:** Administrador seleciona usuário na lista e clica em "Editar".
**Fluxo Principal:**
1. O administrador acessa a tela de edição do usuário;
2. O administrador altera nome, e-mail e/ou status (Ativo/Inativo);
3. O sistema valida unicidade de e-mail se alterado;
4. O sistema atualiza os dados do usuário;
5. O sistema registra a alteração no log de auditoria (RNF009);
6. Caso de uso encerrado.
**Fluxo Alternativo:**
1a. Novo e-mail duplicado: Sistema exibe "E-mail já cadastrado neste domínio";
1b. Usuário não encontrado: Sistema exibe erro.
**Pós-condições:** Dados do usuário atualizados.
**Regras de negócio:** Validação de unicidade de e-mail, log de auditoria.

## UC06: Excluir Usuário
**Objetivo:** Permite que o administrador exclua usuários do domínio.
**Requisitos:** RF004
**Atores:** Administrador
**Prioridade:** Média
**Pré-condições:** Administrador logado; usuário alvo existe; usuário não é o próprio administrador logado.
**Frequência de uso:** Baixa
**Criticalidade:** Alta
**Condição de Entrada:** Administrador seleciona usuário e clica em "Excluir".
**Fluxo Principal:**
1. O administrador confirma a exclusão em dialog de confirmação;
2. O sistema remove o usuário do domínio;
3. O sistema registra a exclusão no log de auditoria;
4. O usuário não aparece mais nas consultas;
5. Caso de uso encerrado.
**Fluxo Alternativo:**
1a. Administrador cancela: Sistema retorna à lista sem excluir;
1b. Tentativa de excluir a si mesmo: Sistema impede com mensagem "Não é possível excluir próprio usuário".
**Pós-condições:** Usuário removido permanentemente.
**Regras de negócio:** Confirmação obrigatória, log de auditoria, proteção auto-exclusão.

## UC07: Cadastrar Colaborador Padrão
**Objetivo:** Permite cadastrar colaborador que recebe apenas salário base.
**Requisitos:** RF005, RF006
**Atores:** Administrador
**Prioridade:** Alta
**Pré-condições:** Administrador logado.
**Frequência de uso:** Alta
**Criticalidade:** Alta
**Condição de Entrada:** Administrador acessa "Colaboradores" > "Novo" e seleciona tipo "Padrão".
**Fluxo Principal:**
1. O administrador acessa tela de cadastro de colaborador;
2. O administrador seleciona tipo "Padrão";
3. O administrador informa matrícula única, nome obrigatório e salário base não negativo;
4. O sistema valida matrícula única (RN001), nome obrigatório (RN002), salário não negativo (RN003);
5. O sistema calcula salário final = salário base automaticamente (RN008);
6. O sistema registra o colaborador;
7. O colaborador aparece na lista com salário final calculado;
8. Caso de uso encerrado.
**Fluxo Alternativo:**
1a. Matrícula duplicada: "Matrícula já cadastrada";
1b. Nome vazio: "Nome é obrigatório";
1c. Salário negativo: "Salário base não pode ser negativo".
**Pós-condições:** Colaborador Padrão cadastrado com salário final calculado.
**Regras de negócio:** RN001, RN002, RN003, RN008. Não permite informar vendas, comissão, produção ou valor unitário.

## UC08: Cadastrar Colaborador Comissionado
**Objetivo:** Permite cadastrar colaborador com remuneração baseada em comissão sobre vendas.
**Requisitos:** RF005, RF007
**Atores:** Administrador
**Prioridade:** Alta
**Pré-condições:** Administrador logado.
**Frequência de uso:** Alta
**Criticalidade:** Alta
**Condição de Entrada:** Administrador acessa "Colaboradores" > "Novo" e seleciona tipo "Comissionado".
**Fluxo Principal:**
1. O administrador acessa tela de cadastro de colaborador;
2. O administrador seleciona tipo "Comissionado";
3. O administrador informa matrícula única, nome, salário base, valor de vendas e percentual de comissão;
4. O sistema valida matrícula única (RN001), nome obrigatório (RN002), salário não negativo (RN003), vendas não negativo (RN004), comissão não negativo (RN005);
5. O sistema calcula salário final = salário base + (vendas × comissão%) automaticamente (RN008);
6. O sistema registra o colaborador;
7. Caso de uso encerrado.
**Fluxo Alternativo:**
1a. Valores negativos: Mensagens específicas por campo (RN004, RN005).
**Pós-condições:** Colaborador Comissionado cadastrado com salário final calculado.
**Regras de negócio:** RN001, RN002, RN003, RN004, RN005, RN008.

## UC09: Cadastrar Colaborador por Produção
**Objetivo:** Permite cadastrar colaborador com remuneração baseada em produção por unidade.
**Requisitos:** RF005, RF008
**Atores:** Administrador
**Prioridade:** Alta
**Pré-condições:** Administrador logado.
**Frequência de uso:** Alta
**Criticalidade:** Alta
**Condição de Entrada:** Administrador acessa "Colaboradores" > "Novo" e seleciona tipo "Produção".
**Fluxo Principal:**
1. O administrador acessa tela de cadastro de colaborador;
2. O administrador seleciona tipo "Produção";
3. O administrador informa matrícula única, nome, salário base, quantidade produzida e valor por unidade;
4. O sistema valida matrícula única (RN001), nome obrigatório (RN002), salário não negativo (RN003), produção não negativa (RN006), valor unidade não negativo (RN007);
5. O sistema calcula salário final = salário base + (quantidade × valor unidade) automaticamente (RN008);
6. O sistema registra o colaborador;
7. Caso de uso encerrado.
**Fluxo Alternativo:**
1a. Valores negativos: Mensagens específicas por campo (RN006, RN007).
**Pós-condições:** Colaborador Produção cadastrado com salário final calculado.
**Regras de negócio:** RN001, RN002, RN003, RN006, RN007, RN008.

## UC10: Consultar Colaboradores
**Objetivo:** Permite visualizar lista de colaboradores com dados cadastrais e remuneratórios.
**Requisitos:** RF009
**Atores:** Administrador, Usuário
**Prioridade:** Alta
**Pré-condições:** Usuário logado; colaboradores cadastrados.
**Frequência de uso:** Muito alta
**Criticalidade:** Média
**Condição de Entrada:** Usuário acessa menu "Colaboradores" > "Consultar".
**Fluxo Principal:**
1. O usuário acessa a tela de consulta de colaboradores;
2. O sistema exibe lista com matrícula, nome, tipo, salário base, dados específicos do tipo e salário final;
3. O usuário pode ordenar por nome ou matrícula;
4. O usuário pode filtrar por tipo (Padrão, Comissionado, Produção);
5. Caso de uso encerrado.
**Fluxo Alternativo:**
1a. Nenhum colaborador: "Nenhum colaborador cadastrado";
1b. Filtro sem resultados: "Nenhum colaborador corresponde ao filtro".
**Pós-condições:** Lista de colaboradores exibida com salários calculados.
**Regras de negócio:** Ordenação e filtro por tipo (RF009).

## UC11: Alterar Colaborador
**Objetivo:** Permite alterar dados cadastrais e remuneratórios de colaboradores.
**Requisitos:** RF013
**Atores:** Administrador
**Prioridade:** Alta
**Pré-condições:** Administrador logado; colaborador alvo existe.
**Frequência de uso:** Média
**Criticalidade:** Alta
**Condição de Entrada:** Administrador seleciona colaborador e clica em "Editar".
**Fluxo Principal:**
1. O administrador acessa tela de edição do colaborador;
2. O administrador altera campos permitidos (todos exceto matrícula);
3. Se alterar tipo de colaborador, sistema solicita dados específicos do novo tipo;
4. O sistema recalcula salário final automaticamente (RN008);
5. O sistema valida regras de negócio conforme novo tipo;
6. O sistema registra alteração no log de auditoria;
7. Caso de uso encerrado.
**Fluxo Alternativo:**
1a. Matrícula alterada: Sistema impede "Matrícula imutável após criação";
1b. Valores negativos: Mensagens específicas por regra de negócio.
**Pós-condições:** Colaborador atualizado com salário recalculado.
**Regras de negócio:** Matrícula imutável, recálculo automático ao alterar variáveis remuneratórias, log de auditoria.

## UC12: Excluir Colaborador
**Objetivo:** Permite excluir colaborador do sistema.
**Requisitos:** RF013
**Atores:** Administrador
**Prioridade:** Média
**Pré-condições:** Administrador logado; colaborador alvo existe.
**Frequência de uso:** Baixa
**Criticalidade:** Alta
**Condição de Entrada:** Administrador seleciona colaborador e clica em "Excluir".
**Fluxo Principal:**
1. O administrador confirma exclusão em dialog de confirmação;
2. O sistema remove o colaborador;
3. O colaborador é removido da folha de pagamento;
4. O sistema registra exclusão no log de auditoria;
5. Caso de uso encerrado.
**Fluxo Alternativo:**
1a. Administrador cancela: Retorna à lista sem excluir.
**Pós-condições:** Colaborador removido permanentemente da folha.
**Regras de negócio:** Confirmação obrigatória, remoção da folha, log de auditoria.

## UC13: Calcular Salário Automaticamente
**Objetivo:** Sistema calcula salário final automaticamente conforme tipo de colaborador.
**Requisitos:** RF010
**Atores:** Sistema (automático)
**Prioridade:** Alta
**Pré-condições:** Colaborador cadastrado ou alterado.
**Frequência de uso:** Muito alta (a cada cadastro/alteração)
**Criticalidade:** Crítica
**Condição de Entrada:** Cadastro ou alteração de qualquer campo remuneratório de colaborador.
**Fluxo Principal:**
1. Sistema detecta criação ou alteração de campo remuneratório;
2. Sistema identifica tipo do colaborador (Padrão, Comissionado, Produção);
3. Se Padrão: salário final = salário base;
4. Se Comissionado: salário final = base + (vendas × comissão%);
5. Se Produção: salário final = base + (quantidade × valor unidade);
6. Sistema atualiza salário final no cadastro;
7. Caso de uso encerrado.
**Fluxo Alternativo:** Nenhum (processo automático).
**Pós-condições:** Salário final calculado e armazenado.
**Regras de negócio:** RN008 (cálculo automático obrigatório, recálculo imediato).

## UC14: Gerar Folha de Pagamento
**Objetivo:** Gera relatório completo da folha de pagamento de todos os colaboradores ativos.
**Requisitos:** RF011
**Atores:** Administrador
**Prioridade:** Alta
**Pré-condições:** Administrador logado; colaboradores cadastrados.
**Frequência de uso:** Mensal/Periódica
**Criticalidade:** Crítica
**Condição de Entrada:** Administrador acessa "Relatórios" > "Folha de Pagamento" > "Gerar".
**Fluxo Principal:**
1. O administrador acessa a tela de geração de folha;
2. O sistema lista todos colaboradores ativos com matrícula, nome, tipo e salário final;
3. O sistema exibe totalizador no rodapé (soma de todos salários finais);
4. O sistema registra data de geração;
5. O administrador pode exportar para PDF ou CSV;
6. Caso de uso encerrado.
**Fluxo Alternativo:**
1a. Nenhum colaborador ativo: Sistema exibe "Nenhum colaborador ativo para gerar folha".
**Pós-condições:** Folha de pagamento gerada com data registrada.
**Regras de negócio:** Apenas colaboradores ativos, totalizador no rodapé, exportação PDF/CSV.

## UC15: Emitir Resumo da Folha
**Objetivo:** Apresenta o valor total consolidado da folha de pagamento.
**Requisitos:** RF012
**Atores:** Administrador
**Prioridade:** Alta
**Pré-condições:** Administrador logado; colaboradores cadastrados.
**Frequência de uso:** Alta (consulta rápida)
**Criticalidade:** Alta
**Condição de Entrada:** Administrador acessa "Relatórios" > "Resumo da Folha".
**Fluxo Principal:**
1. O administrador acessa a tela de resumo da folha;
2. O sistema calcula e exibe o valor total da folha (soma dos salários finais);
3. O valor é exibido em formato monetário brasileiro (R$ 1.234,56);
4. O valor atualiza automaticamente ao alterar cadastros;
5. Caso de uso encerrado.
**Fluxo Alternativo:** Nenhum.
**Pós-condições:** Valor total da folha exibido.
**Regras de negócio:** Formato monetário brasileiro, atualização automática.

## UC16: Excluir Domínio
**Objetivo:** Permite que o administrador exclua o domínio e todos os seus dados.
**Requisitos:** RF014
**Atores:** Administrador
**Prioridade:** Baixa
**Pré-condições:** Administrador logado como único administrador do domínio.
**Frequência de uso:** Muito baixa
**Criticalidade:** Crítica
**Condição de Entrada:** Administrador acessa "Configurações" > "Excluir Domínio".
**Fluxo Principal:**
1. O administrador acessa tela de exclusão de domínio;
2. O sistema exibe aviso de ação irreversível;
3. O administrador confirma primeira vez;
4. O sistema solicita segunda confirmação (confirmação dupla);
5. O administrador confirma segunda vez;
6. O sistema remove: administrador, todos usuários, todos colaboradores;
7. O domínio torna-se inacessível;
8. Caso de uso encerrado.
**Fluxo Alternativo:**
1a. Administrador cancela na primeira confirmação: Retorna sem excluir;
1b. Administrador cancela na segunda confirmação: Retorna sem excluir.
**Pós-condições:** Domínio e todos os dados removidos permanentemente.
**Regras de negócio:** Confirmação dupla obrigatória, ação irreversível, remoção cascata.

## UC17: Visualizar Log de Auditoria
**Objetivo:** Permite que o administrador acesse o histórico de ações do sistema.
**Requisitos:** RNF009
**Atores:** Administrador
**Prioridade:** Média
**Pré-condições:** Administrador logado.
**Frequência de uso:** Baixa/Média
**Criticalidade:** Média
**Condição de Entrada:** Administrador acessa "Auditoria" > "Logs".
**Fluxo Principal:**
1. O administrador acessa a tela de logs de auditoria;
2. O sistema exibe lista com: usuário, ação, timestamp, entidade afetada, valores antes/depois;
3. O administrador pode filtrar por usuário, ação, período, entidade;
4. Os logs são imutáveis e acessíveis apenas a administradores;
5. Caso de uso encerrado.
**Fluxo Alternativo:** Nenhum.
**Pós-condições:** Logs de auditoria exibidos.
**Regras de negócio:** Logs imutáveis, acesso restrito a admin, registro de todas ações (CRUD, relatórios, login/logout).

## UC18: Alterar Própria Senha
**Objetivo:** Permite que qualquer usuário altere sua própria senha.
**Requisitos:** RNF006, RNF007
**Atores:** Administrador, Usuário
**Prioridade:** Média
**Pré-condições:** Usuário logado.
**Frequência de uso:** Baixa
**Criticalidade:** Média
**Condição de Entrada:** Usuário acessa "Perfil" > "Alterar Senha".
**Fluxo Principal:**
1. O usuário acessa tela de alteração de senha;
2. O usuário informa senha atual, nova senha e confirmação;
3. O sistema valida senha atual e força da nova senha (mín. 8 caracteres);
4. O sistema criptografa nova senha com bcrypt;
5. O sistema atualiza a senha;
6. O sistema registra no log de auditoria;
7. Caso de uso encerrado.
**Fluxo Alternativo:**
1a. Senha atual incorreta: "Senha atual incorreta";
1b. Nova senha fraca: Exibe requisitos de senha;
1c. Confirmação não confere: "Senhas não conferem".
**Pós-condições:** Senha atualizada e criptografada.
**Regras de negócio:** RNF006 (bcrypt cost ≥ 12), log de auditoria.

## UC19: Exportar Relatório de Colaboradores
**Objetivo:** Permite exportar lista de colaboradores para PDF ou CSV.
**Requisitos:** RF009, RF011
**Atores:** Administrador
**Prioridade:** Média
**Pré-condições:** Administrador logado; colaboradores cadastrados.
**Frequência de uso:** Média
**Criticalidade:** Baixa
**Condição de Entrada:** Na tela de consulta de colaboradores ou folha, clica em "Exportar".
**Fluxo Principal:**
1. O administrador seleciona formato (PDF ou CSV);
2. O sistema gera arquivo com dados atuais da lista/relatório;
3. O sistema faz download do arquivo;
4. Caso de uso encerrado.
**Fluxo Alternativo:** Nenhum.
**Pós-condições:** Arquivo baixado com dados exportados.
**Regras de negócio:** Dados conforme filtros/ordenação atuais.
