#O sistema devera permitir o cadastro de colaboradores contendo: 
#Matricula 
#Nome 
#Salario Base 
#Tipo de Colaborador  

import array

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

        colaboradores.append(self)

#3.2 Colaborador Comissionado
#Recebe:
#Salário base
#Comissão sobre vendas realizadas
class ColaboradorComissionado(Colaborador):
    
    #O percentual de comissão não poderá ser negativo.
    def __init__(self, matricula:int, nome:str, salario_base:float, percentual_comissao:float) -> None:
        
        self. matricula = matricula
        self.nome = nome
        self.salario_base = salario_base
        self.percentual_comissao = percentual_comissao
        self.valor_de_vendas:float = 0.00

        colaboradores.append(self)

#3.3 Colaborador por Produção
#Recebe:
#Salário base
#Adicional de produtividade
class ColaboradorPorProducao(Colaborador):

    #O valor pago por unidade produzida não poderá ser negativo.
    def __init__(self, matricula:int, nome:str, salario_base:float, valor_por_unidade_produzida:float) -> None:
        
        self. matricula = matricula
        self.nome = nome
        self.salario_base = salario_base
        self.valor_por_unidade_produzida = valor_por_unidade_produzida
        self.quantidade_produzida:int = 0

        colaboradores.append(self)

colaboradores:array = []
