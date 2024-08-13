#Classe de usuario e suas regras 

class User:
    def __init__(self,saldo) -> None:
        self.saldo = float(saldo)
        self.ganhos = int()
        self.derrotas = int()
    
    def adicao_de_saldo(self, adicao_slot):
        soma_total_saldo_multiplicador = self.saldo + adicao_slot
        self.saldo = soma_total_saldo_multiplicador
        self.ganhos += 1
        return self.saldo, self.ganhos
    
    def subtracao_de_saldo(self, sub_slot):
        soma_total_saldo_multiplicador = self.saldo - sub_slot
        self.saldo = soma_total_saldo_multiplicador
        self.derrotas += 1
        return self.saldo, self.derrotas
    
    def multiplicacao_de_saldo(self, multi_slot):
        soma_total_saldo_multiplicador = self.saldo * multi_slot
        self.saldo = soma_total_saldo_multiplicador
        self.ganhos += 1
        return self.saldo, self.ganhos
    
    def mostrar_saldo(self):
        return print(f"Retorno:{self.saldo}, Ganhos:{self.ganhos}, Derrotas:{self.derrotas}")
