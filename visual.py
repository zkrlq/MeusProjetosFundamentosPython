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
janela.title("Calculo do IMC")

# Criação de Elementos da Tela
entrada_altura = ctk.CTkEntry(janela, placeholder_text="Digite a altura em metros")
entrada_peso = ctk.CTkEntry(janela, placeholder_text="Digite o peso em kg")
resultado_botão = ctk.CTkButton(janela, text="Calcular")
resultado = ctk.CTkLabel(janela, text="")

# Posicionamento dos elementos
entrada_altura.pack(pady=20)
entrada_peso.pack(pady=10)  
resultado_botão.pack(pady=10)
resultado.pack(pady=20)








janela.mainloop()

