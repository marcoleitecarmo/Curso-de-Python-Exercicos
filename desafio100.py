from time import sleep
from random import randint


def sorteio(num):
    for c in range(0, 5):
        num.append(randint(1, 10))
    print(f'Foi sorteado 5 números da lista: ', end=' ')
    for g in num:
        print(g, end=' ', flush=True)
        sleep(1)
    print('Resultado!!')


def somaPar(soma):
    som = 0
    for j in soma:
        if j % 2 == 0:
            som += j
    print(f'A soma dos valores pares de {soma}, o resultado é {som}')
    print('-' * 30)


numeros = list()

sorteio(numeros)
somaPar(numeros)
