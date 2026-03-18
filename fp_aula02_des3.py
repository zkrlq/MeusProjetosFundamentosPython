# Autor Enzo
# Desafio 3: Descobrir o preço do metro quadrado de um terreno

# Dados 
comprimento =  float(input("Entre o comprimento do terreno: "))
largura = float(input("Entre a largura do terreno: "))
valor_terreno = 125000

# Calculo da area
resultado_area = comprimento * largura

# Calculo do valor do terreno
resultado_metro =  valor_terreno / resultado_area
print(f"O valor do metro quadrdo é de", {resultado_metro})
