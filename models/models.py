#Classe de usuario e suas regras 
from models.database_models import db
class Betting_House:
    def __init__(self, saldo):
        self.casa_saldo = saldo
        self.saldo_negativo = 0
        self.banca_casa = 0.30
    
    def atualizar_saldo_casa(self, valor):
        self.casa_saldo += valor

    def saldo_casa(self):
        return self.casa_saldo
    

class User:
    def __init__(self, rodadas, user_db_instance, betting_house):
        self.user_db_instance = user_db_instance  # Instância do modelo User_bd
        self.saldo = user_db_instance.saldo
        self.ganhos = 0  # Inicializando com 0
        self.derrotas = 0  # Inicializando com 0
        self.rodadas = int(rodadas)
        self.betting_house = betting_house  # Instância da casa de apostas
        self.layout_grid = []

    def adicao_de_saldo(self, adicao_slot):
        """Adiciona saldo ao usuário quando ele ganha."""
        self.saldo += adicao_slot  # Corrigido para somar ao saldo do usuário
        self.ganhos += 1  # Incrementa o contador de ganhos
        self.betting_house.atualizar_saldo_casa(-adicao_slot)  # A casa paga o usuário
        return self.saldo, self.ganhos

    def subtracao_de_saldo(self, sub_slot):
        """Subtrai saldo do usuário quando ele perde."""
        self.saldo -= sub_slot  # Corrigido para subtrair do saldo do usuário
        self.derrotas += 1  # Incrementa o contador de derrotas
        self.betting_house.atualizar_saldo_casa(sub_slot)  # A casa recebe o valor perdido pelo usuário
        return self.saldo, self.derrotas

    def multiplicacao_de_saldo(self, multi_slot):
        """Multiplica o saldo do usuário quando ele ganha um bônus multiplicador."""
        ganhos = self.saldo * (multi_slot - 1)  # Ganho é o saldo multiplicado menos o saldo original
        self.saldo += ganhos  # Atualiza o saldo do usuário
        self.ganhos += 1  # Incrementa o contador de ganhos
        self.betting_house.atualizar_saldo_casa(-ganhos)  # A casa paga a diferença ao usuário
        return self.saldo, self.ganhos

    def mostrar_saldo(self):
        """Retorna o saldo atual do usuário e seus ganhos/derrotas."""
        return {
            "saldo": self.saldo,
            "ganhos": self.ganhos,
            "derrotas": self.derrotas
        }

    def atualizar_usuario_bd(self):
        """Atualiza o saldo do usuário no banco de dados."""
        self.user_db_instance.saldo = self.saldo
        db.session.commit()

    def add_saldo(self, saldo):
        """Adiciona saldo ao usuário manualmente."""
        self.saldo += saldo