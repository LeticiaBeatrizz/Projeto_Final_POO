import tkinter as tk
from tkinter import messagebox, ttk
from manipulador_de_arquivos.manipulador_reserva import buscar_reserva

class TelaBuscaReserva:
    def __init__(self, container):
        self.criar_widgets(container)

    def criar_abas(self):
        style = ttk.Style()
        style.configure("TNotebook.Tab", padding=[10, 5])
        self.notebook = ttk.Notebook(self.janela)
        self.notebook.pack(expand=True, fill="both")

        aba_reserva = ttk.Frame(self.notebook)
        aba_buscar = ttk.Frame(self.notebook)
        aba_cancelar = ttk.Frame(self.notebook)
        aba_checagem = ttk.Frame(self.notebook)

        self.notebook.add(aba_reserva, text="Reserva")
        self.notebook.add(aba_buscar, text="Buscar")
        self.notebook.add(aba_checagem, text="Checagem")
        self.notebook.add(aba_cancelar, text="Cancelar")

        self.criar_widgets(aba_buscar)
    
    def criar_widgets (self, container,):
        self.label_nome = tk.Label(container, text="Nome do Hóspede:")
        self.label_nome.pack(pady=5)

        self.entrada_nome = tk.Entry(container)
        self.entrada_nome.pack(pady=5)
        self.entrada_nome.focus()

        self.botao = tk.Button(container, text="Buscar", command=self.buscar_reserva)
        self.botao.pack(pady=5)

        self.label_nome_resultado = tk.Label(container)
        self.label_nome_resultado.pack(pady=5)
        
        self.label_cpf_resultado = tk.Label(container, text="CPF:")
        self.label_cpf_resultado.pack(pady=5)
        
        self.label_telefone_resultado= tk.Label(container, text="Telefone:")
        self.label_telefone_resultado.pack(pady=5)
        
        self.label_quarto_resultado = tk.Label(container)
        self.label_quarto_resultado.pack(pady=5)

        self.label_tipo_resultado = tk.Label(container)
        self.label_tipo_resultado.pack(pady=5)

        self.label_dias_resultado = tk.Label(container)
        self.label_dias_resultado.pack(pady=5)

        self.reset_textos_labels()

    def limpar_campos(self):
        self.entrada_nome.delete(0, 'end')

    def reset_textos_labels(self):
        self.label_nome_resultado.config(text="Nome: ")
        self.label_cpf_resultado.config(text="CPF: ")
        self.label_telefone_resultado.config(text="Telefone: ")
        self.label_quarto_resultado.config(text="Quarto: ")
        self.label_tipo_resultado.config(text="Tipo: ")
        self.label_dias_resultado.config(text="Dias: ")

    def exibir_resultado(self, reserva):
        self.reset_textos_labels()
        # Acessa os atributos do objeto Reserva
        self.label_nome_resultado.config(text="Nome: " + reserva.hospede.nome)
        self.label_cpf_resultado.config(text="CPF: " + reserva.hospede.cpf)
        self.label_telefone_resultado.config(text="Telefone: " + str(reserva.hospede.numerotelef))
        self.label_quarto_resultado.config(text="Quarto: " + str(reserva.quarto.numeroquart))
        self.label_tipo_resultado.config(text="Tipo: " + reserva.quarto.tipo)
        self.label_dias_resultado.config(text="Dias: " + str(reserva.dias))

    def buscar_reserva (self):
        nome = self.entrada_nome.get()
        resultado = buscar_reserva(nome)
        if resultado:
            self.exibir_resultado (resultado)
        else:
            self.reset_textos_labels ()
            messagebox.showerror ("Erro", "Reserva não encontrada")
        self.limpar_campos ()
