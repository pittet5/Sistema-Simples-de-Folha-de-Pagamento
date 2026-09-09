import Colaboradores

#3.3 Colaborador por Produção
#Recebe:
#Salário base
#Adicional de produtividade
class ColaboradorPorProducao(Colaboradores.Colaborador):

    #O valor pago por unidade produzida não poderá ser negativo.
    def __init__(self, matricula:int, nome:str, salario_base:float, valor_por_unidade_produzida:float) -> None:
        
        #Checa se a matricula existe
        for col in Colaboradores.colaboradores:
            if col.matricula == matricula:
                return False
        
        self. matricula = matricula

        self.nome = nome

        #Checa se o salario nao eh negativo
        if salario_base < 0:
            return False
        
        self.salario_base = salario_base

        #Checa se o valor por unidade produzida eh negativo
        if valor_por_unidade_produzida < 0.0:
            return False
        
        self.valor_por_unidade_produzida = valor_por_unidade_produzida

        self.quantidade_produzida:int = 0

        Colaboradores.colaboradores.append(self)

        return True