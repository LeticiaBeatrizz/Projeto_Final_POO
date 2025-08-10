from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome: str, cpf: str):
        self.nome = nome
        self.cpf = cpf

    @abstractmethod
    def exibir_dados(self):
        pass
    
    
