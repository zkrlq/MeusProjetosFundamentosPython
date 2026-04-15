# brincadeirinha
import customtkinter as ctk

janela = ctk.CTk()
janela.geometry("400x300")
janela.title("Exemplos Visuais")
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')


# Elementos



entrada1 = ctk.CTkEntry(janela, placeholder_text="Digite algo...", corner_radius=10)
button = ctk.CTkButton(janela, text="Clique aqui", corner_radius=10, hover_color="gray")
entrada1.pack(pady=10)
button.pack(pady=20)
janela.mainloop()