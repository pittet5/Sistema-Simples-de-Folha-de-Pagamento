import array
import email_validator
from enum import Enum

lista_usuarios:array = []

class Permissao(Enum):

    CADASTRAR_COLABORADORES = 1
    LER_COLABORADORES = 2
    ALTERAR_COLABORADORES = 3
    EXCLUIR_COLABORADORES = 4
    CRIAR_USUARIOS = 5
    LER_USUARIOS = 6
    ALTERAR_USUARIOS = 7
    EXCLUIR_USUARIOS = 8
    ALTERAR_NOME_DOMINIO = 9
    EXCLUIR_DOMINIO = 10

class Usuario:

    def __init__(self, login:int, senha:str, permissoes:array):

        self.login = login
        self.senha = senha
        self.permissoes = permissoes

        lista_usuarios.append(self)
    
    @classmethod
    def mudar_senha(self, senha_atual:str, nova_senha:str) -> bool:

        if self.eh_senha_correta(senha_atual):
            self.senha = nova_senha
            return True
        else: return False

    @classmethod
    def eh_senha_correta(self, senha_atual:str) -> bool:

        return True if self.senha == senha_atual else False

    @classmethod
    def possui_permissao(self, permissao:str) -> bool:

        return True if self.permissoes.count(permissao) > 0 else False

class Administrador(Usuario):

    def __init__(self, login:str, senha:str):

        self.login = login
        self.senha = senha
        self.permissoes = []
        
        for perm in Permissao:
            self.permissoes.append(perm)

def login_existe(login:str) -> bool:

    for u in lista_usuarios:
        if u.login == login:
            return True
    
    return False

def usuario_existe(login:str, senha:str) -> bool:

    for u in lista_usuarios:
        if u.login == login and u.senha == senha:
            return True

    return False

def copiar_permissoes(login:int) -> array:

    for u in lista_usuarios:
        if u.login == login:
            return u.permissoes
    
    return []
