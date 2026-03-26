# Autor: Enzo
# Desafio: Calculadora de IMC avançada

while True:

    # Pegando Dados
    peso = float(input("Digite seu Peso: "))
    altura = float(input("Digite sua Altura: "))

    # Calculo
    imc = peso / (altura ** 2)
    print(f"Seu IMC é de, {imc}")

    # Uso do IF
    if imc <= 18.5:
        print(f"Classificação: Abaixo do peso")
    elif imc <= 29.9:
        print(f"Classificação: Normal")
    elif imc <= 34.9:
        print(f"Classificação: Obesidade Grau I")
    elif imc <= 39.9:
        print(f"Classificação: Obesidade Grau II")
    elif imc <= 40:
        print(f"Classificação: Obesidade Grau III")
    else:
        print(f"Algo deu Errado!")

        # Perguntar se o usuário deseja calcular novamente
    resposta = input("Deseja calcular novamente? (s/n): ")
    if resposta.lower() != 's':
        print("Encerrando a calculadora de IMC. Até mais!")
        break