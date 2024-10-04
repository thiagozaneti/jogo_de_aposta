from utils.validations_utils import random_slot, verificar_condicao
from models.models import User, Betting_House
import time


class Roleta:
    def __init__(self, usuario: User, casa: Betting_House):
        self.usuario = usuario
        self.casa = casa

    def rolar_roleta(self, rodadas):
        for c in range(rodadas):
            tempo_inicial = time.time
            print(f"Rodada {c + 1} de {rodadas}")
            self.usuario.subtracao_de_saldo(self.casa.banca_casa)
            self.layout_grid = [
            [random_slot(), random_slot(), random_slot()],
            [random_slot(), random_slot(), random_slot()],
            [random_slot(), random_slot(), random_slot()],
            ]
            for row in self.layout_grid:
                jogada = 0
                self.usuario.layout_grid.append(row)
            print(" |".join(map(str, row)))
            verificar_condicao(self.layout_grid, self.usuario)
            if self.usuario.saldo < self.casa.saldo_negativo:
                break
            tempo_final = time.time
            print(tempo_inicial, tempo_final)
        self.usuario.atualizar_usuario_bd()
        self.usuario.mostrar_saldo()
        self.casa.saldo_casa()
        
        

