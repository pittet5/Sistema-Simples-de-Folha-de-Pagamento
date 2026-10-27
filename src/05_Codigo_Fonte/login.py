import json
import array
import usuarios
from cryptography.fernet import Fernet
from email_validator import validate_email, EmailNotValidError

lista_dominios:dict = {'Pedrolingo': {'Administrador': usuarios.Administrador("pedro@gmail.com", "batata25"), 'Usuarios': [], 'Colaboradores': []}}

class EmailJaExisteErro(Exception):
    """Usuario com este email ja existe"""
    pass

class EmailNaoEhValidoErro(Exception):
    """Email invalido"""
    pass

class UsuarioNaoExisteErro(Exception):
    """Usuario nao existe no sistema"""
    pass

class UsuarioJaExisteErro(Exception):
    """Usuario ja existe no sistema"""
    pass

class SenhaNaoEhValidaErro(Exception):
    """Senha ou usuario incorreto"""
    pass

class DominioNaoExisteErro(Exception):
    """Dominio nao existe no sistema"""
    pass

def criar_novo_administrador(login:str, senha:str) -> usuarios.Administrador:

    if usuarios.login_existe(login):
        return EmailJaExisteErro

    try:
        email_valido = validate_email(login)
        novo_amdmin = usuarios.Administrador(login, senha)
        return novo_amdmin
    except EmailNotValidError:
        return EmailNaoEhValidoErro

def criar_novo_dominio(nome_dominio:str, admin_dominio:usuarios.Administrador) -> bool:

    if lista_dominios.get(nome_dominio) != None:
        return False

    if len(nome_dominio) <= 4:
        return False

    lista_dominios[nome_dominio] = {"Administrador": admin_dominio,
                                    "Usuarios": [],
                                    "Colaboradores": []}

    return True

def criar_novo_usuario_dominio(usuario_espelho:str, login_usuario:str, senha_usuario:str, dominio:str) -> usuarios.Usuario:

    if not usuarios.login_existe(usuario_espelho):
        return UsuarioNaoExisteErro
    
    if usuarios.login_existe(login_usuario):
        return UsuarioJaExisteErro
    
    if lista_dominios.get(dominio) == None:
        return DominioNaoExisteErro

    for usuario in lista_dominios[dominio]['Usuarios']:
        if usuario.login == usuario_espelho:

            novo_usuario = usuarios.Usuario(login_usuario, senha_usuario, usuarios.copiar_permissoes(usuario_espelho))
            lista_dominios[dominio]["Usuarios"].append(novo_usuario)
            return novo_usuario

    if lista_dominios[dominio]['Administrador'].login == usuario_espelho:
        
        novo_usuario = usuarios.Usuario(login_usuario, senha_usuario, usuarios.copiar_permissoes(usuario_espelho))
        lista_dominios[dominio]["Usuarios"].append(novo_usuario)
        return novo_usuario

    return UsuarioNaoExisteErro

def fazer_login(login_usuario:str, senha_usuario:str) -> usuarios.Usuario:

    if not usuarios.usuario_existe(login_usuario, senha_usuario):
        return UsuarioNaoExisteErro

    for usuario in usuarios.lista_usuarios:
        if usuario.login == login_usuario and usuario.senha == senha_usuario:
            return usuario

    return SenhaNaoEhValidaErro

def dominio_do_usuario(usuario:usuarios.Usuario) -> str:

    for dom in lista_dominios:
        for u in lista_dominios[dom]['Usuarios']:
            if u == usuario:
                return dom

    return ''

def dominio_do_administrador(admin:usuarios.Administrador) -> str:

    for dom in lista_dominios:
        if lista_dominios[dom]['Administrador'] == admin:
            return dom

    return ''

def excluir_usuario(usuario:usuarios.Usuario) -> bool:

    dominio_pertencente = dominio_do_usuario(usuario)

    if dominio_pertencente == '':
        return False

    lista_dominios[dominio_pertencente][1].remove(usuario)
    return True
