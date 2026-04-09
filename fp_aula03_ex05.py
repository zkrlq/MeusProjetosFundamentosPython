# Autor: Enzo
# Projeto verificador de Usuario e Senha



# Dados impostos
user = "Enzo"
password = "123456"

# Pegando Dados
usuario = input("Digite seu Usuario: ")
senha = input("Digite sua Senha: ")

# Verificando Usuario e Senha
# AND - Ambas as condições precisam ser verdadeiras para o resultado ser verdadeiro.

if usuario == user and senha == password:
    print("Acesso concedido!, Bem Vindo ao sistema!")
elif usuario != user and senha == password:
    print("Usuario incorreto!, verifique o nome de usuario e tente novamente!")
elif usuario == user and senha != password:
    print("Senha incorreta!, verifique a senha e tente novamente!")
else:
    print("Não foi encontrado nenhum usuario com essas credenciais, tente novamente!")

print("Encerrando o programa. Até mais!")
