# Autor: Enzo
# Projeto calculadora com recebimento de dados do usuario


# Variavel do tipo int é relativa a valores inteiros
# Variavel do tipo float é relativa a valores quebrados
# A palavra reservada input é usada para receber dados do usuario


valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
soma = valor1 + valor2
print('A soma de', valor1, 'e', valor2, 'é igual a: ', soma)

# Para gerar um print com texto preciso que o texto esteja entre asapas.

# Print Formatado usando f-string
# a formatação serve para poder colocar variavel sem precisar da ,
# É obrigatorio utilizar chaves {} para chamar a variavel
print(f'O resultado da soma é: {soma}')
