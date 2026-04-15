# Autor: Enzo
# Projeto: Calculadora de area/valor de um terreno

# Entrada de dados do usuario
comprimento = float(input("Digite o comprimento do terreno: "))
largura = float(input("Digite a largura do terreno: "))
valor_metro = float(input("Digite aqui o valor do metro quadrado: "))

# Calculos
area = comprimento * largura
resultado_metro = valor_metro / area

# Mostrar o resultado
print(f"A Área do terreno é de: ", {area},"")
print(f"O Preço do terreno é de: ",{resultado_metro})

print("Hello Word")
