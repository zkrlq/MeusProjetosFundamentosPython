def verificar_cnh():
    # Autor: Enzo
    # Projeto: Verificar Senhas

    while True:

        # Entrada de dados do usuario
        idade = int(input("Digite sua idade: "))
        bebida = input("Consumiu álcool? (sim/nao): ").lower # .lower evita erros de "sim" "SIM"

        # Verificação
        if idade > 18 and bebida != "nao":
            print("Voce NÃO Pode dirigir!, pois consumiu álcool!")
        elif idade < 18 and bebida != "nao":
            print("Voce NÃO possui 18 anos, e consumiu álcool!")
        elif idade > 18 and bebida == "nao":
            print("Voce pode dirigir, e nao consumiu álcool!")
        elif idade < 18 and bebida != "nao":
            print(f"Voce NÃO possui 18 anos, e consumiu álcool!")
        else:
            print("Voce nao pode dirigir!")

        # Função Loop
        resposta = input("Deseja verificar novamente? (s/n): ").lower()
        if resposta != 's':
            break
verificar_cnh()          