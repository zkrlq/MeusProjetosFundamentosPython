# Fatorial usando 2 Whiles, Verificador de entrada
while True:

# Entrada de Dados
    num = int(input("Digite um número para calcular seu fatorial: "))
    fatorial = 1
    i = 1

# Verificador de entrada
    if num <= 0:
        print("Entrada Invalida, Por favor digite um número positivo")
        continue

# Calculo com While
    while i <= num:
        fatorial *= i
        i += 1
        print(f"O fatorial de {num} é {fatorial}")

# Pergunta para o Loop continuar ou não
    pergunta = input("Deseja calcular o fatorial de outro número? (s/n): ")
    if pergunta != 's':
        break