import os
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
    
    def limpar() -> None:

        os.system('cls||clear')

    def escreva(self, texto:str, texto_limpo=True) -> None:

        if texto_limpo:
            self.limpar()
        
        print(texto)
        self.ultimo_texto = texto

    def adicionar_cursor(self, linha:int = 0) -> str:

        contar_linha = 0

        if linha == contar_linha:
            return ('>'+self.ultimo_texto)
        else:
            contar_linha += 1

        for char_pos, char in enumerate(self.ultimo_texto):
            if char == '\n':
                if linha == contar_linha:
                    return (self.ultimo_texto[:char_pos+1]+'>'+self.ultimo_texto[char_pos+1:])
                else:
                    contar_linha += 1

    def remover_cursor(self) -> str:

        for char_pos, char in enumerate(self.ultimo_texto):
            if char == '>':
                return (self.ultimo_texto[:char_pos]+self.ultimo_texto[char_pos+1:])

    def espere_por_entrada(entrada_esperada:list = []) -> str:

        if len(entrada_esperada) <= 0:

            return ''

        else:

            for entrada in entrada_esperada:

                if keyboard.is_pressed(entrada):
                    return entrada

    def opcoes(pergunta:str, lista_opcoes:set, toggle=False) -> str:

        opcao_atual: int = 0
        texto_ajuda = "mova com as setas [:arrow_up:] e [:arrow_down:] e selecione com [Enter],ou cancele com [Esc]."
    
        opcoes_texto = ""

        for opcao in lista_opcoes:
            opcoes_texto += "\n"+opcao

        return ''
