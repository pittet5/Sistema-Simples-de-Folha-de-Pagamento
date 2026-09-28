import colaboradores
import pandas as pd
from pathlib import Path

def GerarRelatorioDeFolhaDePagamento(nome_arquivo:str):
    
    lista_de_colaboradores:dict = {
        "Matrícula": [],
        "Nome": [],
        "Tipo de Colaborador": [],
        "Salário Base": [],
        "Adicionais": [],
        "Salário Total": []
        }

    for n in range(len(colaboradores.lista_de_colaboradores)):

        col = colaboradores.lista_de_colaboradores[n]

        lista_de_colaboradores["Matrícula"].append(col.matricula)
        lista_de_colaboradores["Nome"].append(col.nome)
        lista_de_colaboradores["Salário Base"].append(col.salario_base)
        match type(col):
            case colaboradores.ColaboradorComissionado:

                salario_adicional:float = col.percentual_comissao * col.valor_de_vendas

                lista_de_colaboradores["Tipo de Colaborador"].append("Comissionado")
                lista_de_colaboradores["Adicionais"].append(salario_adicional)
                lista_de_colaboradores["Salário Total"].append(col.calcular_salario_total)
            case colaboradores.ColaboradorPorProducao:

                salario_adicional:float = col.valor_por_unidade_produzida * col.quantidade_produzida

                lista_de_colaboradores["Tipo de Colaborador"].append("Por Produtividade")
                lista_de_colaboradores["Adicionais"].append(salario_adicional)
                lista_de_colaboradores["Salário Total"].append(col.calcular_salario_total)
            case _:

                lista_de_colaboradores["Tipo de Colaborador"].append("Padrão")
                lista_de_colaboradores["Salário Total"].append(col.calcular_salario_total)
    
    if CriarPasta("Sistema-Simples-de-Folha-de-Pagamento/src/output") == True:

        df = pd.DataFrame(lista_de_colaboradores)

        df.to_excel(f"Sistema-Simples-de-Folha-de-Pagamento/src/output/{nome_arquivo}.xlsx")

def GerarRelatorioResumido(nome_arquivo:str):

    quantidade_colaboradores = len(colaboradores.lista_de_colaboradores)

    valor_total_da_folha:float = 0.00

    valor_total_padrao:float = 0.00
    valor_total_comissionado:float = 0.00
    valor_total_produtividade:float = 0.00

    for col in range(len(colaboradores.lista_de_colaboradores)):

        valor_total_da_folha += col.calcular_salario_total

        match type(col):
            case colaboradores.ColaboradorComissionado:
                valor_total_comissionado += col.calcular_salario_total()
            case colaboradores.ColaboradorPorProducao:
                valor_total_produtividade += col.calcular_salario_total()
            case _:
                valor_total_padrao += col.calcular_salario_total()

    if CriarPasta("Sistema-Simples-de-Folha-de-Pagamento/src/output") == True:

        df = pd.DataFrame({"Quantidade de colaboradores": quantidade_colaboradores,
                        "Valor Total da Folha": valor_total_da_folha,
                        "Valor Total de colaboradores Padrão": valor_total_padrao,
                        "Valor Total de colaboradores Comissionados": valor_total_comissionado,
                        "Valor Total de colaboradores Por Produção": valor_total_produtividade})

        df.to_excel(f"Sistema-Simples-de-Folha-de-Pagamento/src/output/{nome_arquivo}.xlsx")

def CriarPasta(caminho_pasta:str) -> bool:

    nova_pasta = Path(caminho_pasta)

    try:
        nova_pasta.mkdir()
        return True
    except FileExistsError:
        return True
    except PermissionError:
        print(f"Permission denied: Unable to create '{nova_pasta}'.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

