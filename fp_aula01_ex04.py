# Autor: Enzo
# Projeto: Conversor de Temperatura


# Logica
 
# Entrada do usuario em celcius
TempCelcius = float(input("Digite a temperatura em Celcius: "))

# Modulo para converter Fahrenheit
TempFah = (TempCelcius * 1.8) + 32
print("A temperatura em Fahrenheit é", TempFah)

# Modulo para converter Kelvin
TempKel = TempCelcius + 273.15
print("A temperatura em Kelvin é: ", TempKel)
