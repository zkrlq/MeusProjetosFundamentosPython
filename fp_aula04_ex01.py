# Autor: Enzo
# Projeto: Verificar se o condutor possui CNH e se ingeriu alcool

# Função Loop
while True:
        # Dados do usuario
    cnh = input("O condutor possui CNH? (sim/nao): ")
    bafometro = float(input("Qual o valor do bafometro? "))

        # Verificar
    if cnh == "sim" and bafometro < 0.04:
        print(f"O Condutor está apto para dirigir.")
    elif cnh == "nao" and bafometro < 0.04:
        print(f"O Condutor não possui CNH, mas está abaixo do limite")
    elif cnh == "sim" and bafometro >= 0.04:
        print(f"O Condutor possui CNH, mas está acima do limite")
    elif cnh == "nao" and bafometro <= 0.34:
        print(f"O Condutor não possui CNH e está acima do limite")
    else:
        print(f"O Condutor não está apto para dirigir.")

    # Perguntar Loop
    continuar = input("Deseja fazer outra verificação? (sim/nao): ")
    if continuar != "sim":
        break