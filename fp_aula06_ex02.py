# Autor: Enzo
# Loop While - Tabuada
while True:
    num = int(input("Digite um número para ver sua tabuada: "))
    for i in range(1,11):
        print(f"{num} x {i} = {num * i}")

    pergunta = input("Deseja ver a tabuada de outro número? (s/n): ")
    if pergunta.lower() != "s":
        break


    # OU, POde ser feito assim
    """ 
    num = int(input("Digite um número para ver sua tabuada: "))
    i = 1 # ele começa pelo 1
    
    # ENQUANTO i for <= (menor ou igual) 10 faça!
    while i <= 10:
        print(f"{num} x {i} = {num * i}")
        i += 1
    """
    