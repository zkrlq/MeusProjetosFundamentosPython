# Autor: Enzo
# Utilização de Lista e suas funções tais como: Adicionar\Remover\Alterar Itens
def lista_filmes():
    filmes = ['Star Wars','Jurassic Park','Matrix', 'Interestelar']
    print(filmes[2])
    
    filmes.append('Jurassic Park 2')
    print(filmes)

    filmes.insert(2, 'John Wick')
    print(filmes)

    filmes.sort() # .sort deixa em ordem alfabetica.
    print(' | '.join(filmes)) # .join insere algo juntamente do print inicial da lista

lista_filmes()