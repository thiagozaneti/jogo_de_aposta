import random

##falta fazer a randomização de ganhos padrões (em linhas e colunas)

##randomização de ganhos de multipliacação (diagonais)
def random_earnings():
    list_earnings = [1.01,1.02,1.03,1.04,1.05,1.06,1.07,1.08,1.09,1.10]
    weights = [5, 4, 3, 1, 0.5, 0.4, 0.3,0.2,0.1,0.05]
    random.shuffle(weights)
    var_random = random.choices(list_earnings, weights=weights)[0]
    return var_random
