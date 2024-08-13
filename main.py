from utils import random_slot, verificar_condicao
from user import User
import cProfile

saldo_negativo = 0
banca_user = 200
rodadas = 100
usuario = User(banca_user)
banca_casa = 0.20

class Roleta:
    def rolar_roleta(self, rodadas):
        for c in range(rodadas):
            print(f"Rodada {c + 1} de {rodadas}")
            usuario.subtracao_de_saldo(banca_casa)
            self.layout_grid = [
            [random_slot(), random_slot(), random_slot()],
            [random_slot(), random_slot(), random_slot()],
            [random_slot(), random_slot(), random_slot()],
            ]
            for row in self.layout_grid:
                print(" |".join(map(str, row)))
            verificar_condicao(self.layout_grid, usuario)
            if usuario.saldo < saldo_negativo:
                break
        usuario.mostrar_saldo()
        

if __name__ == "__main__":
    roleta_obj = Roleta()
    roleta_obj.rolar_roleta(rodadas=rodadas)
