# Autor: Enzo
"""
   Desafio
    Temos uma lista com 10 alunos
    Em que, 2 desistiram do curso
    1 aluno Entrou
    Devemos ordenar em ordem alfabetica
"""
# Lista Inicial dos Alunos
alunos = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Henry", "Ivy", "Jack"]
print(f"A lista inicial de alunos é de :{len(alunos)} ",', '.join(alunos))

# Remoção Dos Desistentes
alunos.remove("David")
alunos.remove("Frank")  
print(f"A lista após a remoção de desistentes é de : {len(alunos)}, ",', '.join(alunos))

# Aluno Novo entrou
alunos.append("Jose Angelo")
print(f"A lista após a adição do novo aluno é de : {len(alunos)}, ",', '.join(alunos))

# Ordenação em ordem alfabetica
alunos.sort()
print(f"A lista ordenada em ordem alfabetica é de : {len(alunos)}, ",', '.join(alunos))