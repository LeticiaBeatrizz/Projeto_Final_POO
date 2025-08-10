from janelas.janela_principal import TelaLogin
import tkinter as tk

if __name__ == "__main__":
    janela = tk.Tk()
    app = TelaLogin(janela)
    janela.mainloop()
