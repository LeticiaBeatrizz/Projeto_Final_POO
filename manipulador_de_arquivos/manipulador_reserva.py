import os
caminho_arquivo = "arquivos_txt/reservas.txt"

def ler_arquivo (nome_arquivo, modo):
        with open(nome_arquivo, modo) as f:
            conteudo = f.read()
        return conteudo
    
def cadastrar_reserva(nome, cpf, numerotelf, quarto, tipo_quarto, dias):
    try:
        from python.hospede import Hospede
        from python.quarto import Quarto
        from python.reserva import Reserva

        if os.path.exists(caminho_arquivo):
            with open(caminho_arquivo, "r") as arquivo:
                for linha in arquivo:
                    partes = linha.strip().split(';')
                    if len(partes) >= 4:
                        numero_quarto_existente = partes[3].strip()
                        if numero_quarto_existente == str(quarto):
                            return False

        hospede = Hospede(nome, cpf, numerotelf)
        quarto_obj = Quarto(quarto, tipo_quarto)
        reserva = Reserva(hospede, quarto_obj, int(dias))
        linha = f"{reserva.hospede.nome};{reserva.hospede.cpf};{reserva.hospede.numerotelef};{reserva.quarto.numeroquart};{reserva.quarto.tipo};{reserva.dias};{reserva.quarto.ocupado}"
        with open(caminho_arquivo, "a") as arquivo:
            arquivo.write(linha + "\n")
        return True
    except Exception as e:
        print("Erro ao cadastrar:", e)
        return False


def buscar_reserva(nome):
    try:
        from python.hospede import Hospede
        from python.quarto import Quarto
        from python.reserva import Reserva
        with open(caminho_arquivo, "r") as arquivo:
            for linha in arquivo:
                linhaSplitted = linha.strip().split(';')
                if linhaSplitted[0].strip().lower() == nome.strip().lower():
                    
                    nome_hospede = linhaSplitted[0].strip()
                    cpf = linhaSplitted[1].strip()
                    telefone = linhaSplitted[2].strip()
                    numero_quarto = linhaSplitted[3].strip()
                    tipo_quarto = linhaSplitted[4].strip()
                    dias = int(linhaSplitted[5].strip()) if len(linhaSplitted) > 5 and linhaSplitted[5].strip().isdigit() else 1
                    
                    ocupado = False
                    
                    if len(linhaSplitted) > 6:
                        ocupado = linhaSplitted[6].strip().lower() == 'true'

                    hospede = Hospede(nome_hospede, cpf, telefone)
                    
                    quarto = Quarto(numero_quarto, tipo_quarto)
                    quarto.ocupado = ocupado
                    reserva = Reserva(hospede, quarto, dias)
                    
                    reserva.ocupado = ocupado
                    
                    return reserva
        return None
    except Exception as e:
        print("Erro ao buscar:", e)
        return None

def remover_reserva(nome):
    try:
        if not os.path.exists(caminho_arquivo):
            return False

        with open(caminho_arquivo, "r+") as arquivo:
            linhas = arquivo.readlines()
            arquivo.seek(0)
            arquivo.truncate()

            novas_linhas = [linha for linha in linhas if linha.strip().split(";")[0].strip().lower() != nome.lower()]

            arquivo.writelines(novas_linhas)
            return True

    except Exception as e:
        print("Erro ao remover:", e)
        return False
    
def fazer_checkin(nome):
    try:
        if not os.path.exists(caminho_arquivo):
            return None

        reserva = buscar_reserva(nome)
        if reserva is None:
            return None

        sucesso = reserva.check_in()
        if sucesso:
            with open(caminho_arquivo, "r") as arquivo:
                linhas = arquivo.readlines()
            novas_linhas = []
            for linha in linhas:
                partes = linha.strip().split(";")
                if len(partes) >= 1 and partes[0].strip().lower() == nome.strip().lower():
                    partes = partes[:6] + ['True']
                    novas_linhas.append(";".join(partes) + "\n")
                else:
                    novas_linhas.append(linha)
            with open(caminho_arquivo, "w") as arquivo:
                arquivo.writelines(novas_linhas)
            return reserva
        else:
            return None
    except Exception as e:
        print("Erro ao fazer check-in:", e)
        return None


def fazer_checkout(nome):
    try:
        if not os.path.exists(caminho_arquivo):
            return False

        reserva = buscar_reserva(nome)
        if reserva is None:
            return False

        sucesso = reserva.check_out()

        if sucesso:
            with open(caminho_arquivo, "r") as arquivo:
                linhas = arquivo.readlines()
            novas_linhas = []
            for linha in linhas:
                partes = linha.strip().split(";")
                if len(partes) >= 1 and partes[0].strip().lower() == nome.strip().lower():
                    partes = partes[:6] + ['False']
                    novas_linhas.append(";".join(partes) + "\n")
                else:
                    novas_linhas.append(linha)
            with open(caminho_arquivo, "w") as arquivo:
                arquivo.writelines(novas_linhas)
            return True
        else:
            return False
    except Exception as e:
        print("Erro ao fazer check-out:", e)
        return False

        
