import sys
import login
from cli import CLI
from usuarios import Usuario, Administrador

def main():

    cli_principal = CLI()

    while True:

        opcao_login_ou_cadastro = cli_principal.menu("Bem Vindo ao Sistema de Folha de Pagamento!", ["Login", "Cadastrar"])

        print(opcao_login_ou_cadastro)

        if opcao_login_ou_cadastro == '':
            sys.exit(0)

        if opcao_login_ou_cadastro == "Login":

            usuario_sistema:Usuario = None

            while type(usuario_sistema) != Usuario and type(usuario_sistema) != Administrador:

                cli_principal.escreva("Preencha seu usuário e senha.")

                usuario_preenchido = cli_principal.preencher_campo("Usuário")
                senha_preenchida = cli_principal.preencher_campo("Senha", True)

                usuario_sistema = login.fazer_login(usuario_preenchido, senha_preenchida)

                if type(usuario_sistema) != Usuario and type(usuario_sistema) != Administrador:
                    tentar_novamente = cli_principal.instrucoes(["Usuário ou Senha Inválidos."])
                    if tentar_novamente == False:
                        break

            print("Logado com sucesso!")

        if opcao_login_ou_cadastro == "Cadastrar":

            novo_usuario:Administrador = None

            while type(novo_usuario) != Administrador:

                cli_principal.escreva("Escolha seu usuário e senha.")

                usuario_preenchido = cli_principal.preencher_campo("Usuário")
                senha_preenchida = cli_principal.preencher_campo("Senha", True)
                senha_repetida = cli_principal.preencher_campo("Repita a Senha", True)

                if senha_preenchida != senha_repetida:
                    tentar_novamente = cli_principal.instrucoes(["Senhas não coincidem."])
                    if tentar_novamente == False:
                        break
                    else:
                        continue

                novo_usuario = login.criar_novo_administrador(usuario_preenchido, senha_preenchida)

                if type(novo_usuario) != Administrador:
                    tentar_novamente = cli_principal.instrucoes(["Email não é valido ou já está cadastrado no sistema."])
                    if tentar_novamente == False:
                        break

            cli_principal.instrucoes(["Usuário cadastrado com sucesso!", "Prosseguindo para a criação de domínio."])
            
            dominio_criado:bool = False

            while dominio_criado != True:

                cli_principal.escreva("Preencha o nome do seu domínio.")

                nome_dominio = cli_principal.preencher_campo("Domínio")

                dominio_criado = login.criar_novo_dominio(nome_dominio, novo_usuario)

                if dominio_criado == True:
                    break

                cli_principal.instrucoes(["Já existe domínio com este nome ou o nome é inválido."])
