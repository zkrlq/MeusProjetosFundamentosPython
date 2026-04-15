def desconto_cartao():
    # Projeto: Calcular descontos seguindo uma lista

    descontos_roupa = [0.85]
    descontos_movel = [0.90]

    # Calculo de descontos
    preco = input("Digite o Preço do item: ")
    desconto = input("Digite o tipo de desconto (roupa/movel): ").lower

    if desconto == 'roupa':
        preco_desconto = preco * descontos_roupa[0]
    elif desconto == 'movel':
        preco_desconto = preco * descontos_movel[0]
    else:
        print("Tipo de desconto inválido!")
        return

    print(f"O preço com desconto é: {preco_desconto}")