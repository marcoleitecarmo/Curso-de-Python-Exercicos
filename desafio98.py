from time import sleep


def contador(a, b, c):
    if c < 0:
        c *= -1
    if c == 0:
        c = 1
    print('-' * 30)
    print(f'A contagem de {a} até {b} com passo de {c}')
    sleep(1.5)

    if a < b:
        cont = a
        while cont <= b:
            print(f'{cont}', end=' ', flush=True)
            sleep(1)
            cont += c
        print('Fim!!!')
    else:
        cont = a
        while cont >= b:
            print(f'{cont}', end=' ', flush=True)
            sleep(1)
            cont -= c
        print('Fim!!!')


# Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)

print('Personalizando a Contagem')
inicio = int(input('Digite o número inical: '))
fim = int(input('Digite o número final: '))
passos = int(input('Digite o número de passo: '))

contador(inicio, fim, passos)
