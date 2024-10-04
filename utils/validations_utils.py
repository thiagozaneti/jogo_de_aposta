import random
from random_earnings import random_earnings

SUBTRACAO_DE_SALD0 = 1.25

##seleção de tipos da roleta
select_types = ["A","B","C","D","E","F","."]
def random_slot():
    weights = [0.1, 1, 1, 1, 0.5, 0.5, 0.1 ]
    random.shuffle(weights)
    return random.choices(select_types, weights=weights)[0]
##essa função random slot junta uma lista de pesos com o select_types


##função random_earnings - randomiza os ganhos do usuario se ele ganhar na diagonal


##funcao de verificação de linhas - verifica se o usuario ganhou em linhas e colunas em sequencia
def verificar_linhas(layout_grid, usuario):
    ganhou = False
    for i in range(3):
        if layout_grid[i][0] == layout_grid[i][1] == layout_grid[i][2]:
            print(f"Você ganhou na linha {i+1}!")
            usuario.adicao_de_saldo(5)
            ganhou = True
        if layout_grid[0][i] == layout_grid [1][i] == layout_grid[2][i]:
            print(f"Você ganhou na coluna {i+1}!")
            usuario.adicao_de_saldo(5)
            ganhou = True
    return ganhou

##funcao de verificacao de diagonais
def verificar_diagonais(layout_grid, usuario):
    ganhou = False
    if layout_grid[0][0] == layout_grid[1][1] == layout_grid[2][2]:
        print("Obteve multiplicação de saldo na diagonal principal")
        usuario.multiplicacao_de_saldo(random_earnings())
        ganhou = True
    elif layout_grid[0][2] == layout_grid[1][1] == layout_grid[2][0]:
        print("Obteve multiplicação de saldo na diagonal secundária")
        usuario.multiplicacao_de_saldo(random_earnings())
        ganhou = True
    return ganhou


##funcao que verifica todas as condições e aplica a regra na classe de usuario
def verificar_condicao(layout_grid, usuario):
    ganhou_linhas = verificar_linhas(layout_grid, usuario)
    ganhou_diagonais = verificar_diagonais(layout_grid, usuario)

    if not ganhou_linhas or not ganhou_diagonais:
        print("perdeu")
        usuario.subtracao_de_saldo(SUBTRACAO_DE_SALD0)
