# Entrada de dados do usuario
num1 = float(input('Digite aqui o primeiro numero: '))
num2 = float(input('DIgite aqui o segundo numero: '))
operacao = int(input('Digite qual operação realizar (+,-,/,*)'))

# Logica geral
if operacao in ('+', '-', '/', '*'):
    if operacao == '+':
        soma = num1 + num2
        print(f"O Resultado da soma é: {soma}")  
    elif operacao == '-':
        sub = num1 - num2
        print(f'O Resultado da subtração é: {sub}')
    elif operacao == '/':
        div = num1 / num2
        print(f'O Resultado da subtração é: {div}')    
    elif operacao == '*':
        multi = num1 * num2
        print(f"O Resultado da divisão é: {multi}")
    else:
        print('Operação Invalida!')   