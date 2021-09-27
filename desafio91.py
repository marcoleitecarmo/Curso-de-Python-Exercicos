from random import randint
from operator import itemgetter
from time import sleep

jogo = {'jogador 1': randint(1, 6), 'jogador 2': randint(1, 6),
        'jogador 3': randint(1, 6), 'jogador 4': randint(1, 6)}

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

for i, j in jogo.items():
    print(f'{i} tirou {j}')
    sleep(1)
print('-=' * 30)
for i, j in enumerate(ranking):
    print(f'{i+1}º lugar: {j[0]} com {j[1]}')
    sleep(1)
