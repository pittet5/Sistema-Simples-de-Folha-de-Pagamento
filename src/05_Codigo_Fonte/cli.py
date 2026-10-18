import os
import time
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

    def menu(self, texto_menu:str, opcoes:set, icone:str = '', pode_sair:bool=True) -> str:

        menu_completo = ""

        menu_completo = texto_menu

        for opcao in opcoes:
            if type(opcao) is not str:
                opcoes.discard(opcao)

        opcao_atual = 0

        menu_completo += self.gerar_opcoes(opcoes, opcao_atual)

        if pode_sair:
            menu_completo += "Use as setas para mover e 'Enter' para confirmar ou 'Esc' para sair."

        else:
            menu_completo += "Use as setas para mover e 'Enter' para confirmar."

        self.escreva(menu_completo)

        ultima_entrada_recebida = ''

        while True:

            tecla = keyboard.read_event()

            if tecla.event_type == keyboard.KEY_DOWN:
                match tecla.name:
                    case 'escape':
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
                menu_completo += "Use as setas para mover e 'Enter' para confirmar ou 'Esc' para sair."

            else:
                menu_completo += "Use as setas para mover e 'Enter' para confirmar."

            self.escreva(menu_completo)

            if ultima_entrada_recebida == tecla.name:
                time.sleep(0.1)
            else:
                time.sleep(0.25)
            
            ultima_entrada_recebida = tecla.name
