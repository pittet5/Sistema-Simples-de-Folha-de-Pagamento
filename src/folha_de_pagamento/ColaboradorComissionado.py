import Colaboradores

#3.2 Colaborador Comissionado
#Recebe:
#Salário base
#Comissão sobre vendas realizadas
class ColaboradorComissionado(Colaboradores.Colaborador):
    
    #O percentual de comissão não poderá ser negativo.
    def __init__(self, matricula:int, nome:str, salario_base:float, percentual_comissao:float) -> None:
        
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

        #Checa se o percentual de comissao eh negativo
        if percentual_comissao < 0.00:
            return False

        self.percentual_comissao = percentual_comissao

        self.valor_de_vendas:float = 0.00

        Colaboradores.colaboradores.append(self)

        return True