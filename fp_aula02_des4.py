# Autor: Enzo
# Projeto:

"""
A empresa ABC desja melhorar o seu consumo com os carros
A empresa deseja inicialmente analisar o desempenho dos carros
 
A empresa precisa saber se compensa abastecer com etanol ou gasolina

dados devem ser apresentados da seguinte forma:
nome da empresa_modelocarro_combustivel_consumo
formatados com 2 casas decimais.
Gasolina - 6.69 L
Etanol - 4.61 L
 """

# Descobrir se vale a pena mais Gasolina ou Etanol
valor_gasolina = 6.69
valor_etanol = 4.61
resultado = valor_etanol / valor_gasolina
print(f"O Valor da diferença é: {resultado:.2f}")

if resultado > 0.7:
    print("Etanol é mais vantjoso")
else:
    print("Gasolina é mais vantajoso")

print()

# Descobrindo o consumo do carro
distancia = float(input("Digite a distancia percorrida: "))
litros = float(input("Digite a quantidade de litros abastecidos: "))
consumo = distancia / litros
print(f"O consumo do carro é de: ",{consumo})

print()

# Imprimindo do modelo pedido
print(f'ABC', 'CivicG9_Do_jose_angelo', 'Gasolina', {consumo}, sep="_", end=".pdf")
