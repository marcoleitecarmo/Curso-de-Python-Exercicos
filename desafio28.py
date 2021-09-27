from random import randint
from time import sleep
print('Pense em um número inteiro entre 0 e 5 ')
numero = int(input("digite o numero que você ache que o computador escolheu "))
computador = randint(0, 5)
print("Processando...")
sleep(2)
print('O computador escolheu o número {} '.format(computador)) # jogador tenta adivinhar
if numero == computador:
    print('Parabens, você venceu!! ')
else:
    print('Que pena, você perdeu')
