from random import randint
cont = 0
while True:
    n = int(input('Digite seu número: '))
    a = ' '
    while a not in 'PI':
        a = str(input('Escolha PAR ou IMPAR [P/I]: ')).strip().upper()[0]
    c = randint(0, 10)
    if (n + c) % 2 == 0:
        if a == 'P':
            print(f'Você Venceu! Você escolheu {n}, o Computador {c}. A soma deu {c + n} é PAR')
        else:
            print(f'Você Perdeu! Você escolheu {n}, o computador {c}. A soma deu {c + n} é PAR')
            break
    if (n + c) % 2 != 0:
        if a == 'I':
            print(f'Você Venceu! Você escolheu {n}, o Computador {c}. A soma deu {c + n} é IMPAR')
        else:
            print(f'Você Perdeu! Você escolheu {n}, o computador {c}. A soma deu {c + n} é IMPAR')
            break
    cont += 1
print(f'Você venceu {cont} vezes.')
print('O jogo Acabou!!!')

