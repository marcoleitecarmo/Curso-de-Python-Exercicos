from random import randint
from time import sleep
from operator import itemgetter


def lin(msg):
    print('\33c')
    print('-' * 30)
    print(f'{"|": <}{msg:^28}{"|":>}')
    print('-' * 30)


org = list()
jogo = dict()
print('Numeros Sorteados: ')
for c in range(1, 5):
    jogo[f'Jogador {c}'] = randint(1, 6)
for k, v in jogo.items():
    print(f' O {k} tirou: {v}')
    sleep(1)
org = sorted(jogo.items(), key=itemgetter(1), reverse=True)
lin('RANKING')
for i, v in enumerate(org):
    print(f'{i+1}ª lugar: {v[0] } com {v[1]}')
