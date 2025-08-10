from .pessoa import Pessoa

class Hospede(Pessoa):
    def __init__(self, nome, cpf, numerotelef):
        super().__init__(nome, cpf)
        self.numerotelef = numerotelef

    def exibir_dados(self):
        return f"Nome: {self.nome}\nCPF: {self.cpf}\nTelefone: {self.numerotelef}"
