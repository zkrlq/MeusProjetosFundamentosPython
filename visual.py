# Autor: Enzo 
# Projeto Padrão - Visual

# Sempre que formos instalar pacotes utilizaremos -> pip install {nomedopacote} * Sem chaves
# Instalar o pacote do CustomTkinter -> pip install customtkinter

# Importação da biblioteca
# como foi utilizado o as ctk, iremos utilizar ctk quando formos usar algo da biblioteca customtkinter
import customtkinter as ctk

# Configuração da Janela - Padrão - Utilizaremos para todos os projetos.
# Janela é uma variavel que recebe a biblioteca ctk
janela = ctk.CTk()
janela.geometry("800x600")
janela.title("Calculadora de temperatura")

janela.mainloop()

