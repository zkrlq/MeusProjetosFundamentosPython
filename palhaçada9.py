from PIL import Image, ImageTk
import customtkinter as ctk
import os


# Configurações Globais de Tema
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        
                # --- RESOLUÇÃO DO ÍCONE ---
        try:
            caminho_icone = r"C:/Users/49666209888/Downloads/icon.ico"
            img = Image.open(caminho_icone)
            
            # Converte para o formato compatível com o sistema de ícones do Tkinter
            self.icone_objeto = ImageTk.PhotoImage(img) 
            self.wm_iconphoto(False, self.icone_objeto)
        except Exception as e:
            print(f"Erro ao carregar ícone: {e}")
        # ---------------------------



        # Configuração da Janela
        self.title("Calculadora IMC Pro")
        self.geometry("400x500")
        self.resizable(False, False)

        # Layout Centralizado (Grid)
        self.grid_columnconfigure(0, weight=1)
        
        # Título Moderno
        self.titulo = ctk.CTkLabel(self, text="CÁLCULO DE IMC", font=("Roboto", 24, "bold"), text_color="#3b8ed0")
        self.titulo.pack(pady=(30, 20))

        # Container Principal (Card)
        self.container = ctk.CTkFrame(self, fg_color="#2b2b2b", corner_radius=15)
        self.container.pack(pady=10, padx=30, fill="both", expand=True)

        # Inputs com Labels
        self.label_peso = ctk.CTkLabel(self.container, text="Peso Atual (kg):", font=("Roboto", 12))
        self.label_peso.pack(pady=(20, 0), padx=20, anchor="w")
        self.peso_entry = ctk.CTkEntry(self.container, placeholder_text="Ex: 85.5", height=45, border_width=1)
        self.peso_entry.pack(pady=(5, 15), padx=20, fill="x")

        self.label_altura = ctk.CTkLabel(self.container, text="Altura (m):", font=("Roboto", 12))
        self.label_altura.pack(pady=(0, 0), padx=20, anchor="w")
        self.altura_entry = ctk.CTkEntry(self.container, placeholder_text="Ex: 1.75", height=45, border_width=1)
        self.altura_entry.pack(pady=(5, 25), padx=20, fill="x")

        # Botão de Ação Destacado
        self.btn_calcular = ctk.CTkButton(self.container, text="CALCULAR AGORA", font=("Roboto", 14, "bold"), 
                                         height=50, corner_radius=8, command=self.calcular_imc)
        self.btn_calcular.pack(pady=10, padx=20, fill="x")

        # Área de Resultado Estilizada
        self.resultado_txt = ctk.CTkLabel(self.container, text="---", font=("Roboto", 28, "bold"))
        self.resultado_txt.pack(pady=(20, 5))
        
        self.classificacao_txt = ctk.CTkLabel(self.container, text="Aguardando dados...", font=("Roboto", 13))
        self.classificacao_txt.pack(pady=(0, 20))

    def calcular_imc(self):
        try:
            p = float(self.peso_entry.get().replace(',', '.'))
            a = float(self.altura_entry.get().replace(',', '.'))
            imc = p / (a ** 2)
            
            # Atualiza o valor principal
            self.resultado_txt.configure(text=f"{imc:.1f}")
            
            # Lógica de feedback visual por cor
            if imc < 18.5:
                res = "Abaixo do peso"; cor = "#e67e22"
            elif 18.5 <= imc < 25:
                res = "Peso Ideal"; cor = "#2ecc71"
            elif 25 <= imc < 30:
                res = "Sobrepeso"; cor = "#f1c40f"
            else:
                res = "Obesidade"; cor = "#e74c3c"
                
            self.classificacao_txt.configure(text=res, text_color=cor)
            self.resultado_txt.configure(text_color=cor)
            
        except ValueError:
            self.classificacao_txt.configure(text="Erro: Use apenas números!", text_color="#e74c3c")

if __name__ == "__main__":
    app = App()
    app.mainloop()
