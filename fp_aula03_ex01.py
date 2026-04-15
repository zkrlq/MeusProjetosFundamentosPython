# Autor: Enzo
# Projeto Estrutura Condicional

# Entrada de dados
nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
nota3 = float(input("Digite a terceira nota do aluno: "))
nota4 = float(input("Digite a quarta nota do aluno: "))

# Calculo da media
media = (nota1 + nota2 + nota3 + nota4) / 4
print(f"A Media do aluno é {media:.2f}")
# Executando a função
if media >= 5:
    print(f"Aluno Aprovado :p, com media {media:.2f}")
else:
    print(f"Aluno Reprovado :c, com media {media:.2f}")