import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self): # O nome Self, vai ser substituido pelo janela.ctk que foi criado anteriormente
        super().__init__()
        # Configurações Visuais - Janela
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        self.geometry("300x400")
        self.title("Calculo do IMC")


         # Função do Calculo   
        def calcular_imc():
            peso = float(entrada_peso.get().replace(",", "."))  # .replace impede que o codigo de erro caso o usuario digite 1,75 ao inves de 1.75
            altura = float(entrada_altura.get().replace(",", "."))
            imc = peso / (altura ** 2)
            resultado.configure(text=f"IMC: {imc:.2f}")

            # Verificação da Classificação
            if imc < 18.5:
                classificacao.configure(text="Abaixo do peso", text_color="blue")
            elif 18.5 <= imc < 25:
                classificacao.configure(text="Peso normal", text_color="green")
            elif 25 <= imc < 30:
                classificacao.configure(text="Sobrepeso", text_color="orange")
            else:
                classificacao.configure(text="Obesidade", text_color="red")

        # Elementos Da tela
        text_top = ctk.CTkLabel(self, text="Calculadora de IMC", font=("Arial", 16, "bold"))
        entrada_peso = ctk.CTkEntry(self, placeholder_text="Digite o peso em kg", width=220, height=36,corner_radius=10,border_color="#fff",font=("Arial", 12),fg_color="#333")
        entrada_altura = ctk.CTkEntry(self, placeholder_text="Digite a altura em metros", width=220, height=36,corner_radius=10,border_color="#fff",font=("Arial", 12),fg_color="#333")
        resultado_botão = ctk.CTkButton(self, text="Calcular", width=220, height=36, corner_radius=10, border_color="#fff", font=("Arial", 12), fg_color="#007acc", hover_color="#005f9e", command=calcular_imc)
        resultado = ctk.CTkLabel(self, text="")
        classificacao = ctk.CTkLabel(self, text="")


        # Padys
        text_top.pack(pady=10)
        entrada_peso.pack(pady=20)
        entrada_altura.pack(pady=10)
        resultado_botão.pack(pady=10)
        resultado.pack(pady=20)
        classificacao.pack(pady=10)



# Rodar o Loop do Programa
if __name__ == "__main__":
    app = App()
    app.mainloop()