#O sistema devera permitir o cadastro de lista_de_colaboradores contendo: 
#Matricula 
#Nome 
#Salario Base 
#Tipo de Colaborador  

import array

lista_de_colaboradores:array = []

#3.1 Colaborador Padrao
#Recebe apenas o salario base cadastrado.
class Colaborador:

    #Toda matricula devera ser unica dentro do sistema. (Recomendacao para ambiente produtivo.)
    #O nome do colaborador eh obrigatorio.
    #O salario base nao podera ser negativo.
    def __init__(self, matricula:int, nome:str, salario_base:float) -> None:
        
        self.matricula = matricula
        self.nome = nome
        self.salario_base = salario_base

        lista_de_colaboradores.append(self)

    @classmethod
    def calcular_salario_total(self) -> float:

        return self.salario_base

#3.2 Colaborador Comissionado
#Recebe:
#Salário base
#Comissão sobre vendas realizadas
class ColaboradorComissionado(Colaborador):
    
    #O percentual de comissão não poderá ser negativo.
    def __init__(self, matricula:int, nome:str, salario_base:float, percentual_comissao:float) -> None:
        
        self.matricula = matricula
        self.nome = nome
        self.salario_base = salario_base
        self.percentual_comissao = percentual_comissao
        self.valor_de_vendas:float = 0.00

        lista_de_colaboradores.append(self)
        
    @classmethod
    def calcular_salario_total(self) -> float:

        return (self.salario_base + (self.valor_de_vendas * (self.percentual_comissao/100)))

#3.3 Colaborador por Produção
#Recebe:
#Salário base
#Adicional de produtividade
class ColaboradorPorProducao(Colaborador):

    #O valor pago por unidade produzida não poderá ser negativo.
    def __init__(self, matricula:int, nome:str, salario_base:float, valor_por_unidade_produzida:float) -> None:
        
        self.matricula = matricula
        self.nome = nome
        self.salario_base = salario_base
        self.valor_por_unidade_produzida = valor_por_unidade_produzida
        self.quantidade_produzida:int = 0

        lista_de_colaboradores.append(self)
        
    @classmethod
    def calcular_salario_total(self) -> float:

        return (self.salario_base + (self.valor_por_unidade_produzida * self.quantidade_produzida))

def CadastrarColaborador(nome_col:str, salario_col:float, tipo_col:str = "padrao", adicional:float = 0.0) -> bool:

    #Checa se o nome eh valido
    if nome_col.strip() == "":
        return False
    
    #Checa se o salario eh negativo
    if salario_col < 0.0:
        return False

    match tipo_col.lower():
        case "padrao":
            if len(lista_de_colaboradores) < 1:
                novo_colaborador:Colaborador = Colaborador(0, nome_col, salario_col)
            else: novo_colaborador:Colaborador = Colaborador(lista_de_colaboradores[-1].matricula + 1, nome_col, salario_col)
        case "comissionado":
            if adicional < 0.0:
                return False
            
            if len(lista_de_colaboradores) < 1:
                novo_colaborador:ColaboradorComissionado = ColaboradorComissionado(0, nome_col, salario_col, adicional)
            else: novo_colaborador:ColaboradorComissionado = ColaboradorComissionado(lista_de_colaboradores[-1].matricula + 1, nome_col, salario_col, adicional)
        case "produtividade":
            if adicional < 0.0:
                return False
            
            if len(lista_de_colaboradores) < 1:
                novo_colaborador:ColaboradorPorProducao = ColaboradorPorProducao(0, nome_col, salario_col, adicional)
            else: novo_colaborador:ColaboradorPorProducao = ColaboradorPorProducao(lista_de_colaboradores[-1].matricula + 1, nome_col, salario_col, adicional)
        case _:
            if len(lista_de_colaboradores) < 1:
                novo_colaborador:Colaborador = Colaborador(0, nome_col, salario_col)
            else: novo_colaborador:Colaborador = Colaborador(lista_de_colaboradores[-1].matricula + 1, nome_col, salario_col)

def MostrarColaborador(col_matricula:int):
    
    col = EncontrarColaboradores(col_matricula, "")[0]

    match type(col):
        case ColaboradorComissionado():
            print(f"Nome: {col.nome}\nMatrícula: {col.matricula}\nTipo: Comissionado\nSalário Base: {col.salario_base}\nPercentual de Comissão: {col.percentual_comissao}\nValor de Vendas: {col.valor_de_vendas}\nSalário Total: {col.calcular_salario_total()}")
        case ColaboradorPorProducao():
            print(f"Nome: {col.nome}\nMatrícula: {col.matricula}\nTipo: Produtividade\nSalário Base: {col.salario_base}\nValor Por Unidade Produzida: {col.valor_por_unidade_produzida}\nQuantidade Produzia: {col.quantidade_produzida}\nSalário Total: {col.calcular_salario_total()}")
        case Colaborador:
            print(f"Nome: {col.nome}\nMatrícula: {col.matricula}\nTipo: Produtividade\nSalário Base: {col.salario_base}\nSalário Total: {col.calcular_salario_total()}")


def AlterarColaborador(matricula:int, novo_nome:str = "", novo_salario:float = 0.00, novo_tipo:str = "padrao",
                       novo_percentual_comissao:float = 0.00, novo_valor_vendas:float = 0.00,
                       novo_valor_por_producao:float = 0.00, nova_quantidade_produzida:int = 0):
    
    match novo_tipo.strip().lower():
        case "padrao":
            colaborador_modificado:Colaborador = Colaborador(matricula, novo_nome, novo_salario)
            for col in lista_de_colaboradores:
                if col.matricula == matricula:
                    col = colaborador_modificado
        case "comissionado":
            colaborador_modificado:Colaborador = ColaboradorComissionado(matricula, novo_nome, novo_salario, novo_percentual_comissao)
            colaborador_modificado.valor_de_vendas = novo_valor_vendas
            for col in lista_de_colaboradores:
                if col.matricula == matricula:
                    col = colaborador_modificado
        case "produtividade":
            colaborador_modificado:Colaborador = ColaboradorPorProducao(matricula, novo_nome, novo_salario, novo_valor_por_producao)
            colaborador_modificado.quantidade_produzida = nova_quantidade_produzida
            for col in lista_de_colaboradores:
                if col.matricula == matricula:
                    col = colaborador_modificado

def ExcluirColaborador(col_matricula:int) -> bool:

    for col in lista_de_colaboradores:
        if col.matricula == col_matricula:
            lista_de_colaboradores.remove(col)
            return True
    
    return False

def EncontrarColaboradores(buscar_matricula:int, buscar_nome:str) -> array:
    
    lista_de_colaboradores_achados:array = []

    #busca colaborador pela matricula
    for col in lista_de_colaboradores:
        if col.matricula == buscar_matricula:
            lista_de_colaboradores_achados.append(col)
            break
    
    #busca colaborador pelo nome
    for col in lista_de_colaboradores:
        if col.nome.find(buscar_nome):
            if col.nome == buscar_nome:
                lista_de_colaboradores_achados.clear()
                lista_de_colaboradores_achados.append(col)
                break
            lista_de_colaboradores_achados.append(col)

    return lista_de_colaboradores_achados
