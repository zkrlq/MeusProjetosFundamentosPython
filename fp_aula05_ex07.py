# Autor: Enzo
# Desafio: Veriicar se o numero é par ou impar


while True:
        numero = int(input("Digite um numero: "))
    
        if numero % 2 == 0:
            print("O número é par.")
        else:
            print("O número é ímpar.")

        respota = input("Deseja continuar? (s/n): ")
        if respota.lower() != 's':
         break

