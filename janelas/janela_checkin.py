import tkinter as tk
from tkinter import messagebox
from manipulador_de_arquivos.manipulador_reserva import fazer_checkin

class TelaCheckin:
    def __init__(self, container):
        self.criar_widgets(container)
    
    def criar_widgets(self, container):
        self.label_titulo = tk.Label(container, text="Check-in\nInforme o nome do hóspede:")
        self.label_titulo.pack(pady=10)

        self.label_nome = tk.Label(container, text="Nome do Hóspede:")
        self.label_nome.pack(pady=5)

        self.entrada_nome = tk.Entry(container, width=30)
        self.entrada_nome.pack()

        self.botao_checkin = tk.Button(container, text="Fazer Check-in", command=self.realizar_checkin)
        self.botao_checkin.pack(pady=15)

        self.botao_limpar = tk.Button(container, text="Limpar Campo", command=self.limpar_campos)
        self.botao_limpar.pack(pady=5)

    def realizar_checkin(self):
        nome = self.entrada_nome.get().strip()
        resultado = fazer_checkin(nome)
        if resultado:

            messagebox.showinfo("Check-in realizado", f"Check-in realizado para: {nome}")
        else:
            messagebox.showerror("Erro", "Reserva não encontrada para esse nome.")

    def limpar_campos(self):
        self.entrada_nome.delete(0, tk.END)
        
