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
        return print(f"saldo_banca:{self.casa_saldo}")

class User:
    def __init__(self, rodadas, user_db_instance, betting_house):
        self.user_db_instance = user_db_instance  # Instância do modelo User_bd
        self.saldo = user_db_instance.saldo
        self.ganhos = int()
        self.derrotas = int()
        self.rodadas = int(rodadas)
        self.betting_house = betting_house
        

    def adicao_de_saldo(self, adicao_slot):
        soma_total_saldo = self.saldo + adicao_slot
        self.saldo = soma_total_saldo
        self.ganhos += 1
        self.betting_house.atualizar_saldo_casa(-adicao_slot)  
        return self.saldo, self.ganhos

    def subtracao_de_saldo(self, sub_slot):
        soma_total_saldo = (self.saldo - sub_slot)
        self.saldo = soma_total_saldo
        self.derrotas += 1
        self.betting_house.atualizar_saldo_casa(sub_slot)  
        return self.saldo, self.derrotas

    def multiplicacao_de_saldo(self, multi_slot):
        soma_total_saldo = self.saldo * multi_slot
        self.saldo = soma_total_saldo
        self.ganhos += 1
        self.betting_house.atualizar_saldo_casa(-soma_total_saldo + self.saldo)  
        return self.saldo, self.ganhos

    def mostrar_saldo(self):
        return print(f"Retorno Usuário:{self.saldo}, Ganhos:{self.ganhos}, Derrotas:{self.derrotas}")

    def atualizar_usuario_bd(self):
        self.user_db_instance.saldo = self.saldo
        db.session.commit()