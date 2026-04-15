# Autor: Enzo
# Projeto verificar se o cliente tem a credencial vip, e se ele é acima de 18 anos, para ter acesso a um evento exclusivo.


# Entrada de dados do usuario
credencial = input("Digite se voce tem a credencial VIP (sim/nao): ")
idade_usuario = int(input("Digite sua idade: "))

# Verificar os dados
if credencial == "sim" and idade_usuario >= 18:
    print(f"Parabens! Voce Possui acesso")
else:
    print(f"Desculpe, voce nao possui acesso!")
