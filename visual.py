# Autor: Enzo 
# Projeto Padrão - Visual

# Sempre que formos instalar pacotes utilizaremos -> pip install {nomedopacote} * Sem chaves
# Instalar o pacote do CustomTkinter -> pip install customtkinter

# Importação da biblioteca
# como foi utilizado o as ctk, iremos utilizar ctk quando formos usar algo da biblioteca customtkinter
import customtkinter as ctk

# Configuração da Janela - Padrão - Utilizaremos para todos os projetos.
# Janela é uma variavel que recebe a biblioteca ctk

# Configurações Visuais
ctk.set_appearance_mode("dark") # Modos: 'light', 'dark'
ctk.set_default_color_theme('blue') # Temas: "blue", "green", "dark-blue"


janela = ctk.CTk()
janela.geometry("300x300")
janela.title("Calculadora de temperatura")

# Criação de Elementos da Tela
entrada = ctk.CTkEntry(janela, placeholder_text="Digite a temperatura em Celsius")
button = ctk.CTkButton(janela, text="Converter")
label = ctk.CTkLabel(janela, text="Resultado: ")

# Posicionamento dos elementos
entrada.pack(pady=20)
button.pack(pady=10)
label.pack(pady=20)

janela.mainloop()

