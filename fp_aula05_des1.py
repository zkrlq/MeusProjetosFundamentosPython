# Autor: Enzo
# Desafio 1 - Criar um programa de fatorial com loop While/FOR

while True:

      # Entrada de dados do usuario
    numero = int(input("Digite um número: "))
    fatorial = 1

    # Verificar o Input
    if numero <= 0:
        print("Numero inválido! Por favor, digite um número positivo.")
        continue

    # Calculo com o For
    for i in range(1, numero + 1):
        fatorial *= i
        print(f" O fatorial de {numero} é {fatorial}")


    pergunta = input("Deseja calcular o fatorial de outro número? (s/n): ")
    if pergunta.lower() != "s":
        print("Obrigado por usar o programa!, Volte Sempre!")
        break