from .quarto import Quarto
from .hospede import Hospede

class Reserva:
    def __init__(self, hospede: Hospede, quarto: Quarto, dias: int):
        self.hospede = hospede
        self.quarto = quarto
        self.dias = dias

    def check_in(self):
        if self.quarto.ocupado:
            print("Quarto já está ocupado!")
            return False
        self.quarto.ocupado = True
        print(f"Check-in realizado para {self.hospede.nome} no quarto {self.quarto.numeroquart}.")
        self.ocupado = True
        return True

    def check_out(self):
        if not self.ocupado:
            print("Reserva não está ativa.")
            return False
        self.quarto.ocupado = False
        print(f"Check-out realizado para {self.hospede.nome} no quarto {self.quarto.numeroquart}.")
        self.ocupado = False
        return True
    
    def __str__(self):
        status = "Ativa" if self.ocupado else "Finalizada"
        return f"Reserva: {self.hospede.nome} - Quarto {self.quarto.numeroquart} - {self.dias} dias - {status}"
