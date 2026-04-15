# Autor: Enzo
# Desafio: Calulo de fatorial de numero usando loop FOR

# Entrada de dados do usuario
numero = int(input("Digite um número: "))
fatorial = 1


# Calculo com o For
for i in range(1, numero + 1):
    fatorial *= i
    print(f" O fatorial de {numero} é {fatorial}")
