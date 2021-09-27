from random import randint
from time import sleep

print('-=-'*25)
print('\033[1;31mVou Pensar em um Número tente Adivinhar!\033[m:'.center(80))
print('-=-'*25)

escolha = randint(0,10)
tentativas = 0
acertou = False

while not acertou:
    numero = int(input('\033[1;36mDigite um numero: \033[m'))
    print('\033[1;31mHummm Estou Analisando o número......\033[m')
    sleep(1)
    tentativas += 1

    if numero == escolha:
        acertou = True
    else:
        if numero < escolha:
            print('\033[1;32mO número esta baixo, aumente mais um pouco\033[m')

        elif numero > escolha:
            print('\033[1;32mO numero esta alto, diminua um pouco\033[m')
print('\033[1;34mVocê acertou com {} tentativas Parabéns!!!\033[m'.format(tentativas))




