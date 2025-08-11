import tkinter as tk
from tkinter import messagebox, ttk
from manipulador_de_arquivos.manipulador_reserva import cadastrar_reserva
from .janela_buscar import TelaBuscaReserva
from .janela_cancelar import TelaCancelarReserva
from .janela_checkin import TelaCheckin
from .janela_checkout import TelaCheckout

class TelaReserva:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Reserva")
        self.janela.iconbitmap("ico's/ico-janela.ico")

        self.centralizar_janela(400, 350)
        self.criar_abas()
    
    def criar_abas(self):
        style = ttk.Style()
        style.configure("TNotebook.Tab", padding=[10, 5])
        self.notebook = ttk.Notebook(self.janela)
        self.notebook.pack(expand=True, fill="both")

        aba_reserva = ttk.Frame(self.notebook)
        aba_buscar = ttk.Frame(self.notebook)
        aba_cancelar = ttk.Frame(self.notebook)
        aba_checkin = ttk.Frame(self.notebook)
        aba_checkout = ttk.Frame(self.notebook)

        self.notebook.add(aba_reserva, text="Reserva")
        self.notebook.add(aba_buscar, text="Buscar")
        self.notebook.add(aba_checkin, text="Check-in")
        self.notebook.add(aba_checkout, text="Check-out")
        self.notebook.add(aba_cancelar, text="Cancelar")

        self.criar_widgets(aba_reserva)
        TelaBuscaReserva(aba_buscar)
        TelaCancelarReserva(aba_cancelar)
        TelaCheckin(aba_checkin)
        TelaCheckout(aba_checkout)

    def centralizar_janela(self, largura, altura):
        largura_tela = self.janela.winfo_screenwidth()
        altura_tela = self.janela.winfo_screenheight()
        x = (largura_tela // 2) - (largura // 2)
        y = (altura_tela // 2) - (altura // 2)
        self.janela.geometry(f"{largura}x{altura}+{x}+{y}")

    def criar_widgets(self, container):
        self.label_nome = tk.Label(container, text="Nome do Hóspede:")
        self.label_nome.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.entrada_nome = tk.Entry(container, width=30)
        self.entrada_nome.grid(row=0, column=1, padx=50, pady=5)

        self.label_cpf = tk.Label(container, text="CPF:")
        self.label_cpf.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.entrada_cpf = tk.Entry(container, width=20)
        self.entrada_cpf.grid(row=1, column=1, padx=10, pady=5)

        self.label_telefone = tk.Label(container, text="Telefone:")
        self.label_telefone.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.entrada_telefone = tk.Entry(container, width=20)
        self.entrada_telefone.grid(row=2, column=1, padx=10, pady=5)

        self.label_quarto = tk.Label(container, text="Número do Quarto:")
        self.label_quarto.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        self.entrada_quarto = tk.Entry(container, width=10)
        self.entrada_quarto.grid(row=3, column=1, padx=10, pady=5)

        self.label_tipo = tk.Label(container, text="Tipo de Quarto:")
        self.label_tipo.grid(row=4, column=0, padx=10, pady=5, sticky="w")

        opcoes = ["Quarto simples", "Suíte", "Suíte p/casais", "Suíte presidencial"]
        self.combobox = ttk.Combobox(container, values=opcoes)
        self.combobox.grid(row=4, column=1, padx=10, pady=5)
        self.combobox.set("Selecione um quarto")

        self.label_dias = tk.Label(container, text="Dias de Hospedagem:")
        self.label_dias.grid(row=5, column=0, padx=10, pady=5, sticky="w")

        self.entrada_dias = tk.Entry(container, width=10)
        self.entrada_dias.grid(row=5, column=1, padx=10, pady=5)

        self.botao_reservar = tk.Button(container, text="Fazer Reserva", command=self.fazer_reserva)
        self.botao_reservar.grid(row=6, column=0, columnspan=2, pady=15)

        self.botao_limpar = tk.Button(container, text="Limpar Campos", command=self.limpar_campos)
        self.botao_limpar.grid(row=7, column=0, columnspan=2, pady=5)

    def fazer_reserva(self):
        nome = self.entrada_nome.get()
        cpf = self.entrada_cpf.get()
        telefone = self.entrada_telefone.get()
        quarto = self.entrada_quarto.get()
        dias = self.entrada_dias.get()
        tipo_quarto = self.combobox.get()

        if not nome or not cpf or not telefone or not quarto or not tipo_quarto or tipo_quarto == "Selecione um quarto" or not dias:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos!")
            return

        try:
            dias_int = int(dias)
            if cadastrar_reserva(nome, cpf, telefone, quarto, tipo_quarto, dias):
                messagebox.showinfo("Sucesso", "Reserva realizada com sucesso!")
                self.limpar_campos()
                mensagem = "Reserva realizada com sucesso!\n"
                mensagem += f"Hóspede: {nome}\n"
                mensagem += f"CPF: {cpf}\n"
                mensagem += f"Telefone: {telefone}\n"
                mensagem += f"Quarto: {quarto} ({tipo_quarto})\n"
                mensagem += f"Dias: {dias_int}"

        except ValueError:
            messagebox.showerror("Erro", "O campo 'Dias' deve ser um número inteiro!")



    def limpar_campos(self):
        self.entrada_nome.delete(0, tk.END)
        self.entrada_cpf.delete(0, tk.END)
        self.entrada_telefone.delete(0, tk.END)
        self.entrada_quarto.delete(0, tk.END)
        self.combobox.set("Selecione um quarto")
        self.entrada_dias.delete(0, tk.END)
