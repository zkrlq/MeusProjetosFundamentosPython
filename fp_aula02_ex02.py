# Autor: Enzo
# Projeto: Cotação do dolar com casas arredondadas

# Entrada de dados do usuario
real = float(input("Qual o valor em reais: "))

# Calculo
dolar = 5.26
resultado = real / dolar

# Print
print(f"O Valor do dolar hoje, {resultado:.2f}")
