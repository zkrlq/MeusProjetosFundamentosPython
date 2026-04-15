# Autor: Enzo
# Projeto - Utilizando o Básico de Lista

nomes = ["Joao","Maria","Marta","Anakin","Leia"]
print(nomes)
print("\n" + nomes[2])


nomes[3] = 'Cleber' # Altera a posição original do numero 3
print("\n" + str(nomes))

nomes.append('Matheus') # .append é utilizado para incluir coisas na lista
print("\n" + str(nomes))


del nomes[5] # .del é utilizado para remover coisas da lista
print("\n" + str(nomes))
