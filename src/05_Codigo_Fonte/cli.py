import os
import keyboard

def limpar() -> None:

    os.system('cls||clear')

def escreva(texto:str, texto_limpo=True) -> None:

    if texto_limpo:
        limpar()
    
    print(texto)

def opcoes(pergunta:str, lista_opcoes:set, toggle=False) -> str:

    opcao_atual: int = 0
 
    opcoes_texto = pergunta + "\n\n"

    for indice, opcao in enumerate(lista_opcoes):
        if indice == opcao_atual:
            opcoes_texto += ">" + opcao + "\n"
        else:
            opcoes_texto += opcao + "\n"

    opcoes_texto += "mova com as setas [:arrow_up:] e [:arrow_down:] e selecione com [Enter],ou cancele com [Esc]."

    escreva(opcoes_texto)

    while not keyboard.is_pressed('esc'):

        if keyboard.is_pressed('up'):
            if opcao_atual == 0:
                opcao_atual = len(lista_opcoes)-1
            else:
                opcao_atual -= 1
                
            escreva(opcoes_texto)
            continue
        
        if keyboard.is_pressed('down'):
            if opcao_atual == len(lista_opcoes)-1:
                opcao_atual = 0
            else:
                opcao_atual += 1
                
            escreva(opcoes_texto)
            continue
        
        if keyboard.is_pressed('enter'):
            return lista_opcoes[opcao_atual]
    
    return ''

escreva(opcoes("Qual opção deseja?", ["opção 1", "opção 2", "opção 3"]))
