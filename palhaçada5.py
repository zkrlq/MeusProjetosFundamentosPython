# Autor: Enzo
# Desafio Pegar 10 numeros, e verificar se eles são positivos ou negativos usando If e For
total_positivo = 0
total_negativo = 0
lista_numeros = []

for i in range(4):
    numero = int(input("Digite um número: "))
    lista_numeros.append(numero)


# Verificar se o numero é positivo ou negativo
for n in lista_numeros:
    if n > 0:
        print(f"{n} é positivo.")
        total_positivo += 1
    elif n < 0:
        print(f"{n} é negativo.")
        total_negativo += 1
    else:
        print(f"{n} é neutro.")


print()

# Verificar se os numeros sao impares ou par
total_par = 0
total_impar = 0

for n in lista_numeros:
    if n % 2 == 0:
        print(f"{n} é par.")
        total_par += 1
    else:
        print(f"{n} é ímpar.")
        total_impar += 1


print(f"\nTotal de números positivos: {total_positivo}")
print(f"Total de números negativos: {total_negativo}")
print(f"Total de números pares: {total_par}")
print(f"Total de números ímpares: {total_impar}")