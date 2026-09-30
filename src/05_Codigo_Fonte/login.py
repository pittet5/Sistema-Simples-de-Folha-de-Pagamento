import json
import array
import usuarios
from cryptography.fernet import Fernet
from email_validator import email_validator, EmailNotValidError

lista_dominios:dict = {}

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

def criar_novo_administrador(login:str, senha:str) -> usuarios.Administrador:

    if usuarios.login_existe(login):
        return EmailJaExisteErro

    try:
        email_valido = email_validator(login)
        novo_amdmin = usuarios.Administrador(login, senha)
        return novo_amdmin
    except EmailNotValidError:
        return EmailNaoEhValidoErro

def criar_novo_dominio(nome_dominio:str, admin_dominio:usuarios.Administrador) -> bool:

    if lista_dominios.get(nome_dominio) != None:
        return False

    lista_dominios[nome_dominio] = {"Administrador": admin_dominio,
                                    "Usuarios": {},
                                    "Colaboradores": {}}

    return True

def criar_novo_usuario_dominio(usuario_espelho:int, login_usuario:int, senha_usuario:str) -> usuarios.Usuario:

    if not usuarios.login_existe(usuario_espelho):
        return UsuarioNaoExisteErro
    
    if usuarios.login_existe(login_usuario):
        return UsuarioJaExisteErro
    
    novo_usuario = usuarios.Usuario(login_usuario, senha_usuario, usuarios.copiar_permissoe(usuario_espelho))
    return novo_usuario
