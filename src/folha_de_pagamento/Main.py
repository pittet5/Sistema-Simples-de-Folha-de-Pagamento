import Colaboradores
import array
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

def MostrarColaborador(col_matricula:int):
    
    col:Colaboradores.Colaborador = EncontrarColaboradores(col_matricula, "")[0]

    match type(col):
        case Colaboradores.ColaboradorComissionado:
            print(f"Nome: {col.nome}\nMatrícula: {col.matricula}\nTipo: Comissionado\nSalário Base: {col.salario_base}\nPercentual de Comissão: {col.percentual_comissao}\nValor de Vendas: {col.valor_de_vendas}\nSalário Total: {col.salario_base + (col.valor_de_vendas * (col.percentual_comissao / 100))}")
        case Colaboradores.ColaboradorPorProducao:
            print(f"Nome: {col.nome}\nMatrícula: {col.matricula}\nTipo: Produtividade\nSalário Base: {col.salario_base}\nValor Por Unidade Produzida: {col.valor_por_unidade_produzida}\nQuantidade Produzia: {col.quantidade_produzida}\nSalário Total: {col.salario_base + (col.quantidade_produzida * col.valor_por_unidade_produzida)}")
        case _:
            print(f"Nome: {col.nome}\nMatrícula: {col.matricula}\nTipo: Produtividade\nSalário Base: {col.salario_base}\nSalário Total: {col.salario_base}")


def AlterarColaborador(matricula:int, novo_nome:str = "", novo_salario:float = 0.00, novo_tipo:str = "padrao",
                       novo_percentual_comissao:float = 0.00, novo_valor_vendas:float = 0.00,
                       novo_valor_por_producao:float = 0.00, nova_quantidade_produzida:int = 0):
    
    match novo_tipo.strip().lower():
        case "padrao":
            colaborador_modificado:Colaboradores.Colaborador = Colaboradores.Colaborador(matricula, novo_nome, novo_salario)
            for col in Colaboradores.colaboradores:
                if col.matricula == matricula:
                    col = colaborador_modificado
        case "comissionado":
            colaborador_modificado:Colaboradores.Colaborador = Colaboradores.ColaboradorComissionado(matricula, novo_nome, novo_salario, novo_percentual_comissao)
            colaborador_modificado.valor_de_vendas = novo_valor_vendas
            for col in Colaboradores.colaboradores:
                if col.matricula == matricula:
                    col = colaborador_modificado
        case "produtividade":
            colaborador_modificado:Colaboradores.Colaborador = Colaboradores.ColaboradorPorProducao(matricula, novo_nome, novo_salario, novo_valor_por_producao)
            colaborador_modificado.quantidade_produzida = nova_quantidade_produzida
            for col in Colaboradores.colaboradores:
                if col.matricula == matricula:
                    col = colaborador_modificado

def ExcluirColaborador(col_matricula:int) -> bool:

    for col in Colaboradores.colaboradores:
        if col.matricula == col_matricula:
            Colaboradores.colaboradores.remove(col)
            return True
    
    return False

def EncontrarColaboradores(buscar_matricula:int, buscar_nome:str) -> array:
    
    colaboradores_achados:array = []

    #busca colaborador pela matricula
    for col in Colaboradores.colaboradores:
        if col.matricula == buscar_matricula:
            colaboradores_achados.append(col)
            break
    
    #busca colaborador pelo nome
    for col in Colaboradores.colaboradores:
        if col.nome.find(buscar_nome):
            if col.nome == buscar_nome:
                colaboradores_achados.clear()
                colaboradores_achados.append(col)
                break
            colaboradores_achados.append(col)

    return colaboradores_achados

def GerarTabelaDeColaboradores(nome_arquivo:str, inicio:int = 0, qntd:int = 500) -> None:

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

    df.to_excel(f"Sistema-Simples-de-Folha-de-Pagamento/src/output/{nome_arquivo}.xlsx")
