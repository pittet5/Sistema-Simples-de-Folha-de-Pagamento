import Colaboradores

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
                novo_colaborador:Colaborador = Colaboradores.Colaborador(0, nome_col, salario_col)
            else: novo_colaborador:Colaborador = Colaboradores.Colaborador(Colaboradores.colaboradores[-1].matricula + 1, nome_col, salario_col)
        case "comissionado":
            if adicional < 0.0:
                return False
            
            if len(Colaboradores.colaboradores) < 1:
                novo_colaborador:Colaborador = Colaboradores.ColaboradorComissionado(0, nome_col, salario_col, adicional)
            else: novo_colaborador:Colaborador = Colaboradores.ColaboradorComissionado(Colaboradores.colaboradores[-1].matricula + 1, nome_col, salario_col, adicional)
        case "produtividade":
            if adicional < 0.0:
                return False
            
            if len(Colaboradores.colaboradores) < 1:
                novo_colaborador:Colaborador = Colaboradores.ColaboradorPorProducao(0, nome_col, salario_col, adicional)
            else: novo_colaborador:Colaborador = Colaboradores.ColaboradorPorProducao(Colaboradores.colaboradores[-1].matricula + 1, nome_col, salario_col, adicional)
        case _:
            if len(Colaboradores.colaboradores) < 1:
                novo_colaborador:Colaborador = Colaboradores.Colaborador(0, nome_col, salario_col)
            else: novo_colaborador:Colaborador = Colaboradores.Colaborador(Colaboradores.colaboradores[-1].matricula + 1, nome_col, salario_col)

def MostrarColaboradores(inicio:int = 0, qntd:int = 10) -> None:

    if (inicio < 0) or (qntd < 0):
        return

    print("Matrícula    Nome    Salário Base    Tipo    Comissão    Produtividade   Salário Final")

    for col in range(inicio, inicio + qntd):

        if len(Colaboradores.colaboradores) < col + 1:
            return

        colaborador = Colaboradores.colaboradores[col]

        print(f"{colaborador.matricula}", end = "   ")
        print(f"{colaborador.nome}", end = "    ")
        print(f"{colaborador.salario_base}", end = "    ")
        match type(colaborador):
            case Colaboradores.Colaborador:
                print(f"Padrão", end = "    ")
                print(f"{colaborador.salario_base}")
            case Colaboradores.ColaboradorComissionado:
                print(f"Comissionado", end = "    ")

                salario_adicional:float = colaborador.percentual_comissao * colaborador.valor_de_vendas

                print(f"{salario_adicional}", end = "    ")
                print(f"{colaborador.salario_base + salario_adicional}", end = "    \n")
            case Colaboradores.ColaboradorPorProducao:
                print(f"Produção", end = "    ")

                salario_adicional:float = colaborador.valor_por_unidade_produzida * colaborador.quantidade_produzida
                
                print(f"{salario_adicional}", end = "    ")
                print(f"{colaborador.salario_base + salario_adicional}", end = "    \n")

MostrarColaboradores(0, 10)
CadastrarColaborador("Pedro", 2000.00, "Padrao")
CadastrarColaborador("Ashlee", 2500.00, "Comissionado", 10.0)
CadastrarColaborador("Paulo Cesar", 3500.00, "Padrao")
MostrarColaboradores(0, 10)
