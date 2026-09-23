import Colaboradores
import pandas as pd

def CadastrarColaborador(nome_col:str, salario_col:float, tipo_col:str = "padrao", adicional:float = 0.0) -> bool:

    #Checa se o nome eh valido
    if nome_col.strip() == "":
        return False
    
    #Checa se o salario eh negativo
    if salario_col < 0.0:
        return False

    match tipo_col.lower():
        case "padrao":
            if len(Colaboradores.colaboradores) < 1:
                novo_colaborador:Colaboradores.Colaborador = Colaboradores.Colaborador(0, nome_col, salario_col)
            else: novo_colaborador:Colaboradores.Colaborador = Colaboradores.Colaborador(Colaboradores.colaboradores[-1].matricula + 1, nome_col, salario_col)
        case "comissionado":
            if adicional < 0.0:
                return False
            
            if len(Colaboradores.colaboradores) < 1:
                novo_colaborador:Colaboradores.ColaboradorComissionado = Colaboradores.ColaboradorComissionado(0, nome_col, salario_col, adicional)
            else: novo_colaborador:Colaboradores.ColaboradorComissionado = Colaboradores.ColaboradorComissionado(Colaboradores.colaboradores[-1].matricula + 1, nome_col, salario_col, adicional)
        case "produtividade":
            if adicional < 0.0:
                return False
            
            if len(Colaboradores.colaboradores) < 1:
                novo_colaborador:Colaboradores.ColaboradorPorProducao = Colaboradores.ColaboradorPorProducao(0, nome_col, salario_col, adicional)
            else: novo_colaborador:Colaboradores.ColaboradorPorProducao = Colaboradores.ColaboradorPorProducao(Colaboradores.colaboradores[-1].matricula + 1, nome_col, salario_col, adicional)
        case _:
            if len(Colaboradores.colaboradores) < 1:
                novo_colaborador:Colaboradores.Colaborador = Colaboradores.Colaborador(0, nome_col, salario_col)
            else: novo_colaborador:Colaboradores.Colaborador = Colaboradores.Colaborador(Colaboradores.colaboradores[-1].matricula + 1, nome_col, salario_col)

def MostrarColaboradores(inicio:int = 0, qntd:int = 500) -> None:

    lista_de_colaboradores:dict = {
        "Matrícula": [],
        "Nome": [],
        "Tipo de Colaborador": [],
        "Salário Base": [],
        "Percentual de Comissão": [],
        "Valor de Vendas": [],
        "Valor por Produção": [],
        "Quantidade Produzida": [],
        "Salário Total": []
        }

    for n in range(inicio, inicio+qntd):

        col = Colaboradores.colaboradores[n]

        lista_de_colaboradores["Matrícula"].append(col.matricula)
        lista_de_colaboradores["Nome"].append(col.nome)
        match type(col):
            case Colaboradores.ColaboradorComissionado:

                salario_adicional:float = col.percentual_comissao * col.valor_de_vendas

                lista_de_colaboradores["Tipo de Colaborador"].append("Comissionado")
                lista_de_colaboradores["Salário Base"].append(col.salario_base)
                lista_de_colaboradores["Percentual de Comissão"].append(col.percentual_comissao)
                lista_de_colaboradores["Valor de Vendas"].append(col.valor_de_vendas)
                lista_de_colaboradores["Valor por Produção"].append(0.00)
                lista_de_colaboradores["Quantidade Produzida"].append(0)
                lista_de_colaboradores["Salário Total"].append(col.salario_base + salario_adicional)
            case Colaboradores.ColaboradorPorProducao:

                salario_adicional:float = col.valor_por_unidade_produzida * col.quantidade_produzida

                lista_de_colaboradores["Tipo de Colaborador"].append("Por Produtividade")
                lista_de_colaboradores["Salário Base"].append(col.salario_base)
                lista_de_colaboradores["Percentual de Comissão"].append(0.00)
                lista_de_colaboradores["Valor de Vendas"].append(0.00)
                lista_de_colaboradores["Valor por Produção"].append(col.valor_por_unidade_produzida)
                lista_de_colaboradores["Quantidade Produzida"].append(col.quantidade_produzida)
                lista_de_colaboradores["Salário Total"].append(col.salario_base + salario_adicional)
            case _:

                lista_de_colaboradores["Tipo de Colaborador"].append("Padrão")
                lista_de_colaboradores["Salário Base"].append(col.salario_base)
                lista_de_colaboradores["Percentual de Comissão"].append(0.00)
                lista_de_colaboradores["Valor de Vendas"].append(0.00)
                lista_de_colaboradores["Valor por Produção"].append(0.00)
                lista_de_colaboradores["Quantidade Produzida"].append(0)
                lista_de_colaboradores["Salário Total"].append(col.salario_base)
    
    df = pd.DataFrame(lista_de_colaboradores)

    df.to_excel(f"src/output/Lista de Colaboradores {inicio}-{inicio+qntd}.xlsx")

CadastrarColaborador("Pedro", 2000.00, "padrao")
CadastrarColaborador("Ashlee", 2500.00, "commisao", 10.0)
CadastrarColaborador("Paulo Cesar", 3000.00, "padrao")
MostrarColaboradores(0,3)
