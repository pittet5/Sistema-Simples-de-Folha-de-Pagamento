import sys
import login
from cli import CLI
from folha_de_pagamento import GerarRelatorioDeFolhaDePagamento, GerarRelatorioResumido
from usuarios import Usuario, Administrador, Permissao, possui_permissao, tipo_permissao
from colaboradores import TipoColaborador, cadastrar_colaborador

def main():

    cli_login = CLI()

    while True:

        opcao_login_ou_cadastro = cli_login.menu("Bem Vindo ao Sistema de Folha de Pagamento!", ["Login", "Cadastrar"])

        if opcao_login_ou_cadastro == '':
            sys.exit(0)

        if opcao_login_ou_cadastro == "Login":

            usuario_sistema:Usuario = None

            while type(usuario_sistema) != Usuario and type(usuario_sistema) != Administrador:

                cli_login.escreva("Preencha seu usuário e senha.")

                usuario_preenchido = cli_login.preencher_campo("Usuário")
                senha_preenchida = cli_login.preencher_campo("Senha", True)

                usuario_sistema = login.fazer_login(usuario_preenchido, senha_preenchida)

                if type(usuario_sistema) != Usuario and type(usuario_sistema) != Administrador:
                    tentar_novamente = cli_login.instrucoes(["Usuário ou Senha Inválidos."])
                    if tentar_novamente == False:
                        break

            if type(usuario_sistema) == Administrador:
                login_administrador(usuario_sistema)

            else:
                login_usuario(usuario_sistema)

        if opcao_login_ou_cadastro == "Cadastrar":

            novo_usuario:Administrador = None

            while type(novo_usuario) != Administrador:

                cli_login.escreva("Escolha seu usuário e senha.")

                usuario_preenchido = cli_login.preencher_campo("Usuário")
                senha_preenchida = cli_login.preencher_campo("Senha", True)
                senha_repetida = cli_login.preencher_campo("Repita a Senha", True)

                if senha_preenchida != senha_repetida:
                    tentar_novamente = cli_login.instrucoes(["Senhas não coincidem."])
                    if tentar_novamente == False:
                        break
                    else:
                        continue

                novo_usuario = login.criar_novo_administrador(usuario_preenchido, senha_preenchida)

                if type(novo_usuario) != Administrador:
                    tentar_novamente = cli_login.instrucoes(["Email não é valido ou já está cadastrado no sistema."])
                    if tentar_novamente == False:
                        break

            cli_login.instrucoes(["Usuário cadastrado com sucesso!", "Prosseguindo para a criação de domínio."])
            
            dominio_criado:bool = False

            while dominio_criado != True:

                cli_login.escreva("Preencha o nome do seu domínio.")

                nome_dominio = cli_login.preencher_campo("Domínio")

                dominio_criado = login.criar_novo_dominio(nome_dominio, novo_usuario)

                if dominio_criado == True:
                    break

                cli_login.instrucoes(["Já existe domínio com este nome ou o nome é inválido."])

def login_administrador(admin:Administrador) -> Administrador:

    cli_sistema = CLI()

    nome_dominio = login.dominio_do_administrador(admin)

    cli_sistema.instrucoes([f"Bem Vindo ao Sistema de {nome_dominio}"])

    while True:

        opcao_usuario = cli_sistema.menu(f"Sistema de {nome_dominio}", ["Relatórios", "Colaboradores", "Usuários", "Opções de Domínio", "Sair"])

        match opcao_usuario:

            case 'Relatórios':
                tela_relatorios(admin)

            case 'Colaboradores':
                tela_colaboradores(admin)

            case 'Usuários':
                tela_usuarios(admin)

            case 'Opções de Domínio':
                tela_dominio(admin)

            case 'Sair':
                import colaboradores
                colaboradores.lista_de_colaboradores = []
                return admin

def login_usuario(usuario:Usuario) -> Usuario:

    cli_sistema = CLI()

    nome_dominio = login.dominio_do_usuario(usuario)

    cli_sistema.instrucoes([f"Bem Vindo ao Sistema de {nome_dominio}"])

    while True:

        lista_opcoes_usuario = ["Relatórios"]

        for perm in range(1, 5):
            if possui_permissao(usuario, Permissao(perm)):
                lista_opcoes_usuario.append("Colaboradores")
                break

        for perm in range(5, 9):
            if possui_permissao(usuario, Permissao(perm)):
                lista_opcoes_usuario.append("Usuários")
                break
        
        for perm in range(9, 11):
            if possui_permissao(usuario, Permissao(perm)):
                lista_opcoes_usuario.append("Opções de Domíino")
                break

        lista_opcoes_usuario.append("Sair")
        
        opcao_escolhida = cli_sistema.menu(f"Sistema {nome_dominio}", lista_opcoes_usuario)

        match opcao_escolhida:

            case 'Relatórios':
                tela_relatorios(usuario)

            case 'Colaboradores':
                tela_colaboradores(usuario)

            case 'Usuários':
                tela_usuarios(usuario)

            case 'Opções de Domínio':
                tela_dominio(usuario)

            case 'Sair':
                import colaboradores
                colaboradores.lista_de_colaboradores = []
                return usuario

def tela_relatorios(usuario:Usuario) -> None:

    cli_relatorio = CLI()

    opcao_relatorio = cli_relatorio.menu("Selecione a opção de relatório.", ["Relatório Completo", "Relatório Resumido", "Sair"])

    match opcao_relatorio:

        case 'Relatório Completo':

            nome_arquivo = cli_relatorio.preencher_campo("Nome do arquivo")

            GerarRelatorioDeFolhaDePagamento(nome_arquivo)

        case 'Relatório Resumido':

            nome_arquivo = cli_relatorio.preencher_campo("Nome do arquivo")

            GerarRelatorioResumido(nome_arquivo)

def tela_colaboradores(usuario:Usuario) -> None:

    cli_colaboradores = CLI()

    lista_opcoes = []

    for perm in Permissao:
        if possui_permissao(usuario, perm):
            match perm:
                case Permissao.CADASTRAR_COLABORADORES:
                    lista_opcoes.append("Cadastrar Novo Colaborador")
                case Permissao.LER_COLABORADORES:
                    lista_opcoes.append("Procurar Colaborador")

    lista_opcoes.append("Sair")

    while True:

        opcao_escolhida = cli_colaboradores.menu("Cadastre novos colaboradores ou altere colaboradores existentes.", lista_opcoes)

        match opcao_escolhida:

            case 'Cadastrar Novo Colaborador':
                tela_cadastro_colaborador(usuario)

            case 'Sair':
                break

def tela_cadastro_colaborador(usuario:Usuario) -> None:

    cli_cadastro = CLI()

    novo_colaborador: bool = False

    while novo_colaborador == False:

        cli_cadastro.escreva("Preencha os dados do novo colaborador.")

        nome_colaborador = cli_cadastro.preencher_campo("Nome do Colaborador")

        cli_cadastro.escreva(f"Preencha os dados do novo colaborador.\n\nNome do Colaborador: {nome_colaborador}")
        
        salario_colaborador = cli_cadastro.preencher_campo("Salário do Colaborador")

        while type(salario_colaborador != float):

            try:
                salario_colaborador = float(salario_colaborador)
                break

            except ValueError:
                salario_colaborador = cli_cadastro.preencher_campo("Salário do Colaborador")

        cli_cadastro.escreva(f"Preencha os dados do novo colaborador.\n\nNome do Colaborador: {nome_colaborador}\nSalário do Colaborador: {salario_colaborador}")
        
        tipo_colaborador = cli_cadastro.menu("Qual será o tipo do novo colaborador?", ["Padrão", "Comissionado", "Por Produção"])

        match tipo_colaborador:
            case "Padrão":
                novo_colaborador = cadastrar_colaborador(nome_colaborador, salario_colaborador)

            case "Comissionado":
                 cli_cadastro.escreva(f"Preencha os dados do novo colaborador.\n\nNome do Colaborador: {nome_colaborador}\nSalário do Colaborador: {salario_colaborador}\nTipo do Colaborador: {tipo_colaborador}")

                 adicional_colaborador = cli_cadastro.preencher_campo("Adicional de Comissão (%)")

                 novo_colaborador = cadastrar_colaborador(nome_colaborador, salario_colaborador, TipoColaborador.Comissionado, adicional_colaborador)

            case "Por Produção":
                 cli_cadastro.escreva(f"Preencha os dados do novo colaborador.\n\nNome do Colaborador: {nome_colaborador}\nSalário do Colaborador: {salario_colaborador}\nTipo do Colaborador: {tipo_colaborador}")

                 adicional_colaborador = cli_cadastro.preencher_campo("Adicional por Produção")

                 novo_colaborador = cadastrar_colaborador(nome_colaborador, salario_colaborador, TipoColaborador.Produtividade, adicional_colaborador)

def tela_usuarios(usuario:Usuario) -> None:

    cli_usuarios = CLI()

    lista_opcoes = []

    for perm in Permissao:
        if possui_permissao(usuario, perm):
            match perm:
                case Permissao.CRIAR_USUARIOS:
                    lista_opcoes.append("Cadastrar Novo Usuario")
                case Permissao.LER_USUARIOS:
                    lista_opcoes.append("Procurar Usuario")

    lista_opcoes.append("Sair")

    while True:

        opcao_escolhida = cli_usuarios.menu("Cadastre novos usuários ou altere usuários existentes.", lista_opcoes)

        match opcao_escolhida:

            case 'Cadastrar Novo Usuario':
                tela_cadastro_usuario(usuario)

            case 'Sair':
                break

def tela_cadastro_usuario(usuario:Usuario) -> None:

    cli_cadastro = CLI()

    novo_usuario:Usuario = None

    while type(novo_usuario) != Usuario:

        cli_cadastro.escreva("Cadastre o novo usuario.")

        usuario_preenchido = cli_cadastro.preencher_campo("Usuário")
        senha_preenchida = cli_cadastro.preencher_campo("Senha", True)
        espelho_preenchido = cli_cadastro.preencher_campo("Usuário Espelho")

        if type(usuario) == Administrador:
            novo_usuario = login.criar_novo_usuario_dominio(espelho_preenchido, usuario_preenchido, senha_preenchida, login.dominio_do_administrador(usuario))
        else:
            novo_usuario = login.criar_novo_usuario_dominio(espelho_preenchido, usuario_preenchido, senha_preenchida, login.dominio_do_usuario(usuario))

        match novo_usuario:

            case login.UsuarioJaExisteErro:
                tentar_novamente = cli_cadastro.instrucoes(["Usuário já está cadastrado no sistema."])
                if tentar_novamente == False:
                    break

            case login.UsuarioNaoExisteErro:
                tentar_novamente = cli_cadastro.instrucoes(["Usuário espelho não existe no sistema."])
                if tentar_novamente == False:
                    break

            case login.DominioNaoExisteErro:
                tentar_novamente = cli_cadastro.instrucoes(["Erro de domínio."])
                if tentar_novamente == False:
                    break

            case _:
                cli_cadastro.instrucoes(["Usuário cadastrado com sucesso!"])
                break

def tela_dominio(usuario:Usuario) -> None:

    pass
