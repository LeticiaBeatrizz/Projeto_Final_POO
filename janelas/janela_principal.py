import tkinter as tk
from tkinter import messagebox
from python.login import Login
from janelas.janela_reserva import TelaReserva

class TelaLogin:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Login do administrador")
        self.janela.iconbitmap("ico's/ico-janela.ico")
        self.login_service = Login(None, None)
        self.criar_widgets()
        self.centralizar_janela (380,250)
        
    def centralizar_janela (self, largura, altura):
        largura_tela = self.janela.winfo_screenwidth ()
        altura_tela = self.janela.winfo_screenheight ()
        
        x = (largura_tela // 2) - (largura // 2)
        y = (altura_tela // 2) - (altura // 2)
        
        self.janela.geometry (f"{largura}x{altura}+{x}+{y}")

    def criar_widgets(self):
        self.label_login1 = tk.Label(self.janela, text="Seja bem-vindo ao Hotel Horizone!\nInsira abaixo seu usuário e senha para começarmos a gerenciá-lo!")
        self.label_login1.grid(row=0, column=0, sticky="nesw", columnspan=2, pady=(5, 20), padx=13)

        self.label_usuario = tk.Label(self.janela, text="Usuário:")
        self.label_usuario.grid(row=2, column=0, sticky="e", padx=(10,5))

        self.entrada_usuario = tk.Entry(self.janela)
        self.entrada_usuario.grid(row=2, column=1, sticky="w", padx=(5,10), pady=5)

        self.label_senha = tk.Label(self.janela, text="Senha:")
        self.label_senha.grid(row=3, column=0, sticky="e", padx=(10,5), pady=5)

        self.entrada_senha = tk.Entry(self.janela, show="*")
        self.entrada_senha.grid(row=3, column=1, sticky="w", padx=(5,10), pady=5)

        self.botao_login = tk.Button(self.janela, text="Login", command=self.verificar_login)
        self.botao_login.grid(row=4, column=0, columnspan=2, pady=20)
        
    def verificar_login(self):
        usuario = self.entrada_usuario.get()
        senha = self.entrada_senha.get()

        if self.login_service.verificar_login(usuario, senha):
            messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
            self.janela.destroy()
        
            nova_janela = tk.Tk()
            TelaReserva(nova_janela)
            nova_janela.mainloop()
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos.")
