import customtkinter as ctk
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Configurações Globais
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("IMC Pro - Analytics Edition")
        self.geometry("900x600")
        
        # Dados de histórico (memória temporária)
        self.historico_imc = []
        self.ultimo_resultado = {"imc": 0, "status": "Nenhum", "cor": "#3b8ed0"}

        # Configuração de Layout (Grid 1x2)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- SIDEBAR ---
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        
        self.logo_label = ctk.CTkLabel(self.sidebar, text="IMC PRO", font=("Roboto", 24, "bold"))
        self.logo_label.pack(pady=30, padx=20)

        self.btn_calc = ctk.CTkButton(self.sidebar, text="Calculadora", command=self.show_calculadora)
        self.btn_calc.pack(pady=10, padx=20)

        self.btn_dash = ctk.CTkButton(self.sidebar, text="Dashboard", command=self.show_dashboard)
        self.btn_dash.pack(pady=10, padx=20)

        # Toggle de Tema
        self.appearance_mode_label = ctk.CTkLabel(self.sidebar, text="Modo de Exibição:", anchor="w")
        self.appearance_mode_label.pack(side="bottom", padx=20, pady=(0, 5))
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.sidebar, values=["Dark", "Light"], command=self.change_appearance_mode)
        self.appearance_mode_optionemenu.pack(side="bottom", padx=20, pady=(0, 30))

        # --- CONTAINERS DE PÁGINAS ---
        self.frame_calculadora = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.frame_dashboard = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")

        self.setup_calculadora()
        self.show_calculadora() # Página inicial

    def setup_calculadora(self):
        """Estrutura a tela de cálculos"""
        container = ctk.CTkFrame(self.frame_calculadora, fg_color="#2b2b2b", corner_radius=15)
        container.place(relx=0.5, rely=0.5, anchor="center")

        ctk.CTkLabel(container, text="NOVO CÁLCULO", font=("Roboto", 20, "bold")).pack(pady=20)

        self.peso_entry = ctk.CTkEntry(container, placeholder_text="Peso (kg)", width=200, height=40)
        self.peso_entry.pack(pady=10, padx=40)

        self.altura_entry = ctk.CTkEntry(container, placeholder_text="Altura (m)", width=200, height=40)
        self.altura_entry.pack(pady=10, padx=40)

        ctk.CTkButton(container, text="CALCULAR", command=self.calcular_imc, height=40).pack(pady=20)

        self.res_label = ctk.CTkLabel(container, text="---", font=("Roboto", 32, "bold"))
        self.res_label.pack()

        self.status_label = ctk.CTkLabel(container, text="Aguardando dados...", font=("Roboto", 14))
        self.status_label.pack(pady=(0, 20))

        self.btn_salvar = ctk.CTkButton(container, text="Salvar Resultado", state="disabled", command=self.salvar_arquivo)
        self.btn_salvar.pack(pady=10)

    def calcular_imc(self):
        try:
            p = float(self.peso_entry.get().replace(',', '.'))
            a = float(self.altura_entry.get().replace(',', '.'))
            imc = p / (a ** 2)
            
            if imc < 18.5: res, cor = "Abaixo do peso", "#e67e22"
            elif 18.5 <= imc < 25: res, cor = "Peso Ideal", "#2ecc71"
            elif 25 <= imc < 30: res, cor = "Sobrepeso", "#f1c40f"
            else: res, cor = "Obesidade", "#e74c3c"
                
            self.res_label.configure(text=f"{imc:.1f}", text_color=cor)
            self.status_label.configure(text=res, text_color=cor)
            self.btn_salvar.configure(state="normal")
            
            # Atualiza dados para o Dashboard
            self.ultimo_resultado = {"imc": imc, "status": res, "cor": cor}
            self.historico_imc.append(imc)
            
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

    def setup_dashboard(self):
        """Gera o gráfico e a visualização de dados"""
        # Limpa o frame para atualizar o gráfico
        for widget in self.frame_dashboard.winfo_children():
            widget.destroy()

        ctk.CTkLabel(self.frame_dashboard, text="DASHBOARD DE EVOLUÇÃO", font=("Roboto", 24, "bold")).pack(pady=20)

        if not self.historico_imc:
            ctk.CTkLabel(self.frame_dashboard, text="Realize um cálculo primeiro para ver o gráfico.").pack(expand=True)
            return

        # Criando o gráfico com Matplotlib
        fig, ax = plt.subplots(figsize=(5, 3), dpi=100)
        fig.patch.set_facecolor('#1a1a1a') # Fundo dark
        ax.set_facecolor('#1a1a1a')
        
        ax.plot(self.historico_imc, marker='o', color=self.ultimo_resultado['cor'], linewidth=2)
        ax.set_title("Histórico de IMC", color="white")
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')

        canvas = FigureCanvasTkAgg(fig, master=self.frame_dashboard)
        canvas.draw()
        canvas.get_tk_widget().pack(pady=20, padx=20, fill="both", expand=True)

    def salvar_arquivo(self):
        file = filedialog.asksaveasfile(defaultextension=".txt", 
                                        filetypes=[("Arquivo de Texto", "*.txt"), ("Todos os arquivos", "*.*")])
        if file:
            conteúdo = f"RELATÓRIO IMC\nResultado: {self.ultimo_resultado['imc']:.2f}\nStatus: {self.ultimo_resultado['status']}"
            file.write(conteúdo)
            file.close()
            messagebox.showinfo("Sucesso", "Resultado salvo com sucesso!")

    # --- NAVEGAÇÃO ---
    def show_calculadora(self):
        self.frame_dashboard.grid_forget()
        self.frame_calculadora.grid(row=0, column=1, sticky="nsew")

    def show_dashboard(self):
        self.frame_calculadora.grid_forget()
        self.frame_dashboard.grid(row=0, column=1, sticky="nsew")
        self.setup_dashboard()

    def change_appearance_mode(self, new_mode: str):
        ctk.set_appearance_mode(new_mode)

if __name__ == "__main__":
    app = App()
    app.mainloop()
