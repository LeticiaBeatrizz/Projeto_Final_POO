class Login:
    def __init__(self, entrada_usuario, entrada_senha):
        self.entrada_usuario = entrada_usuario
        self.entrada_senha = entrada_senha

    def verificar_login(self, usuario, senha):
        if usuario == "admin" and senha == "1234":
            return True
        else:
            return False
