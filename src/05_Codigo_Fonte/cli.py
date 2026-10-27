import os
import time
from getpass import getpass
import keyboard
from enum import Enum

class PosicaoCursor(Enum):

    LINHA = 0
    GRADE = 1
    CONTINUO = 2

class CLI:

    def __init__(self, cursor:PosicaoCursor = 0) -> None:
        
        self.tipo_cursor = cursor
        self.posicao_cursor = -1
        self.ultimo_texto = ''
    
    def limpar(self) -> None:

        os.system('cls||clear')

    def escreva(self, texto:str, texto_limpo=True) -> None:

        if texto_limpo:
            self.limpar()
        
        print(texto)
        self.ultimo_texto = texto

    def adicionar_cursor(self, texto:str, linha:int = 0) -> str:

        texto_cursor = ''

        if texto == '':
            texto_cursor = self.ultimo_texto
        else:
            texto_cursor = texto

        contar_linha = 0

        if linha == contar_linha:
            return ('>'+texto_cursor)
        else:
            contar_linha += 1

        for char_pos, char in enumerate(texto_cursor):
            if char == '\n':
                if linha == contar_linha:
                    return (texto_cursor[:char_pos+1]+'>'+texto_cursor[char_pos+1:])
                else:
                    contar_linha += 1

    def remover_cursor(self) -> str:

        for char_pos, char in enumerate(self.ultimo_texto):
            if char == '>':
                return (self.ultimo_texto[:char_pos]+self.ultimo_texto[char_pos+1:])

    def gerar_opcoes(self, lista_opcoes:set, opcao_atual:int = 0) -> str:
    
        opcoes_texto = "\n"

        for opcao in lista_opcoes:
            opcoes_texto += "\n"+opcao

        opcoes_texto = self.adicionar_cursor(opcoes_texto, 2+opcao_atual)

        return opcoes_texto

    def menu(self, texto_menu:str, opcoes:set, icone:str = '', pode_sair:bool=True, toggle:bool=False) -> str:

        menu_completo = ""

        menu_completo = texto_menu

        for opcao in opcoes:
            if type(opcao) is not str:
                opcoes.discard(opcao)

        opcao_atual = 0

        menu_completo += self.gerar_opcoes(opcoes, opcao_atual)

        if pode_sair:
            menu_completo += "\n\nUse as setas para mover e 'Enter' para confirmar ou 'Esc' para sair."

        else:
            menu_completo += "\n\nUse as setas para mover e 'Enter' para confirmar."

        self.escreva(menu_completo)

        ultima_entrada_recebida = ''

        while True:

            tecla = keyboard.read_event()

            if tecla.event_type == keyboard.KEY_DOWN:
                match tecla.name:
                    case 'esc':
                        if pode_sair:
                            return ''
                    case 'enter':
                        return opcoes[opcao_atual]
                    case 'up':
                        if opcao_atual == 0:
                            opcao_atual = len(opcoes)-1
                        else:
                            opcao_atual -= 1
                    case 'down':
                        if opcao_atual == len(opcoes)-1:
                            opcao_atual = 0
                        else:
                            opcao_atual += 1
                    case _:
                        continue

            menu_completo = ""

            menu_completo = texto_menu

            menu_completo += self.gerar_opcoes(opcoes, opcao_atual)

            if pode_sair:
                menu_completo += "\n\nUse as setas para mover e 'Enter' para confirmar ou 'Esc' para sair."

            else:
                menu_completo += "\n\nUse as setas para mover e 'Enter' para confirmar."

            self.escreva(menu_completo)

            if ultima_entrada_recebida == tecla.name:
                time.sleep(0.1)
            else:
                time.sleep(0.25)
            
            ultima_entrada_recebida = tecla.name

    def instrucoes(self, lista_instrucoes:set, icone:str='') -> bool:

        texto_instrucoes = ""
        instrucao_atual = 0

        if len(lista_instrucoes) <= 0:
            return False

        texto_instrucoes = lista_instrucoes[instrucao_atual]

        if instrucao_atual == len(lista_instrucoes)-1:
            texto_instrucoes += "\n\nPresione 'Enter' para confirmar."
        else:
            texto_instrucoes += "\n\nAvance com '>' ou retorne com '<'."

        if instrucao_atual == 0:
            texto_instrucoes += " Pressione 'Esc' para sair"

        self.escreva(texto_instrucoes)

        ultima_entrada_recebida = ''

        while True:

            tecla = keyboard.read_event()

            if tecla.event_type == keyboard.KEY_DOWN:

                if tecla.name == 'esc' and instrucao_atual == 0:
                    return False

                if tecla.name == 'enter' and instrucao_atual == len(lista_instrucoes)-1:
                    input()
                    return True

                if tecla.name == 'right' and instrucao_atual != len(lista_instrucoes)-1:
                    instrucao_atual += 1

                if tecla.name == 'left' and instrucao_atual != 0:
                    instrucao_atual -= 1

            texto_instrucoes = lista_instrucoes[instrucao_atual]

            if instrucao_atual == len(lista_instrucoes)-1:
                texto_instrucoes += "\n\nPresione 'Enter' para confirmar."
            else:
                texto_instrucoes += "\n\nAvance com '>' ou retorne com '<'."

            if instrucao_atual == 0:
                texto_instrucoes += " Pressione 'Esc' para sair"

            self.escreva(texto_instrucoes)
            
            if ultima_entrada_recebida == tecla.name:
                time.sleep(0.05)
            else:
                time.sleep(0.15)
            
            ultima_entrada_recebida = tecla.name

    def preencher_campo(self, nome_campo:str, oculto:bool = False) -> str:
        
        while keyboard._pressed_events:
            time.sleep(0.05)

        campo_preenchido:str = ""

        while campo_preenchido.strip() == "":

            if oculto:
                campo_preenchido = getpass("\n"+nome_campo+"  ", echo_char="*")
            else:
                campo_preenchido = input("\n"+nome_campo+"  ")

            if campo_preenchido.strip() != "":
                return campo_preenchido

            self.escreva(self.ultimo_texto)
