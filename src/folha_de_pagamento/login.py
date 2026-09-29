import json
import array
import usuarios
from cryptography.fernet import Fernet

lista_dominios:dict = {}

def criar_novo_dominio(nome_dominio:str, admin_dominio:usuarios.Administrador) -> bool:

    if lista_dominios.get(nome_dominio) != None:
        return False

    lista_dominios[nome_dominio] = {"Administrador": admin_dominio,
                                    "Usuarios": {},
                                    "Colaboradores": {}}

    return True

def criar_novo_administrador(login:int, senha:str) -> usuarios.Administrador:

    novo_amdmin = usuarios.Administrador(login, senha)
    return novo_amdmin
