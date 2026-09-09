import array

#O sistema deverá permitir o cadastro de colaboradores contendo: 
#Matrícula 
#Nome 
#Salário Base 
#Tipo de Colaborador  
class Colaborador:

    #Toda matrícula deverá ser única dentro do sistema. (Recomendação para ambiente produtivo.)
    #O nome do colaborador é obrigatório.
    #O salário base não poderá ser negativo.
    #O salário base não poderá ser negativo.
    def __init__(self, matricula:int, nome:str, salario_base:float) -> None:
        
        #Checa se a matricula existe
        for col in colaboradores:
            if col.matricula == matricula:
                return False
        
        self. matricula = matricula

        self.nome = nome

        #Checa se o salario nao eh negativo
        if salario_base < 0:
            return False
        
        self.salario_base = salario_base

        colaboradores.append(self)

        return True

    

colaboradores:array = []
