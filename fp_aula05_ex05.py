# Autor Enzo
# Projeto: Fazer o calculo de 3 Tabuadas diferentes, com entrada do usuario, e imprimir elas em formato de tabela alinhadas


# Inicio Loop 
while  True:


    # Captura os 3 valores do usuário
    v1 = int(input("Digite o 1º número: "))
    v2 = int(input("Digite o 2º número: "))
    v3 = int(input("Digite o 3º número: "))


# Verificador de Entrada de Usuario
    if v1 <= 0 or v2 <= 0 or v3 <= 0:
        print("Entrada Invalida!, Digite apenas numeros positivos.")
        continue

    print(f"\nTabuadas de {v1}, {v2} e {v3} lado a lado:\n")

    linha = 1

# O while controla as 10 linhas (multiplicadores)
    while linha <= 10:
   
    # Imprime a linha atual para as três tabuadas na mesma linha horizontal
    # Usamos o end="  |  " nos dois primeiros para não pular linha
     print(f"{v1} x {linha:2d} = {v1*linha:2d}", end="  |  ")
     print(f"{v2} x {linha:2d} = {v2*linha:2d}", end="  |  ")
     print(f"{v3} x {linha:2d} = {v3*linha:2d}")

     linha += 1

# Pergunta Loop
    pergunta = input("Deseja continuar? (s/n): ")
    if pergunta.lower() != "s":
        break