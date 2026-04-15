# Autor: Enzo
# Projeto: Calculadora da hipotenusa


# Entrada de dados do usuario
catop = float(input("Entre o valor do cateto oposto: "))
catadj = float(input("Entre o valor do cateto adjacente: "))

# Calculo da Hipotenusa
hip = (catop ** 2 + catadj ** 2) ** 0.5

# Exibir o numero formatado com duas casa decimais
print(f"O valor da hipotenusa é, {hip:.2f}")

# round()
# Arredondar 2 casas.
hip = round(hip, 2)
print(f"O valor da hipotenusa é", {hip})

