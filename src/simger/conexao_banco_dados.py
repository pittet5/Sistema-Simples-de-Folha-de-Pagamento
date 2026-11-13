import sqlite3

def conectar_banco_dados(nome_do_banco:str) -> sqlite3.Connection:

    return sqlite3.connect(fr"src\06_Banco_Dados\{nome_do_banco}.db")

