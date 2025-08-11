import tkinter as tk
from tkinter import messagebox, ttk
from manipulador_de_arquivos.manipulador_reserva import remover_reserva

class TelaCancelarReserva:
    def __init__(self, container):
        self.criar_widgets(container)
        
    def criar_widgets(self, container):
        self.label_titulo = tk.Label(container, text="Cancelar Reserva\nInforme o nome do hóspede:")
        self.label_titulo.pack(pady=10)
        
        self.label_nome = tk.Label(container, text="Nome do Hóspede:")
        self.label_nome.pack(pady=5)
        
        self.entrada_nome = tk.Entry(container, width=30)
        self.entrada_nome.pack()
        
        self.botao_cancelar = tk.Button(container, text="Cancelar Reserva", command=self.cancelar_reserva)
        self.botao_cancelar.pack(pady=15)
        
        self.botao_limpar = tk.Button(container, text="Limpar Campo", command=self.limpar_campos)
        self.botao_limpar.pack(pady=5)

    def cancelar_reserva(self):
        nome = self.entrada_nome.get().strip()
        if not nome:
            messagebox.showerror("Erro", "Por favor, informe o nome do hóspede!")
            return

        sucesso = remover_reserva(nome)
        if sucesso:
            messagebox.showinfo("Sucesso", "Reserva cancelada com sucesso!")
            self.limpar_campos()
        else:
            messagebox.showinfo("Não encontrado", "Reserva não encontrada para o nome informado.")

    def limpar_campos(self):
        self.entrada_nome.delete(0, tk.END)
