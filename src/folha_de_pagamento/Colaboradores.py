class Colaborador:
    def __init__(self, matricula, nome, salario_base) -> None:
        self.matricula = matricula
        self.nome = nome
        self.salario_base = salario_base


novo_colaborador = Colaborador()

print(novo_colaborador.nome)
