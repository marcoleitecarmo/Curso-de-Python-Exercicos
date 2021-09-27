from time import sleep


def maior(*num):
    print('-' * 30)
    print('Analizando os Valores...')
    sleep(1.5)
    for c in num:
        print(f'{c}', end=' ', flush=True)
        sleep(1)
    print(f'Foram passados {len(num)} valores ao todo')
    sleep(1)
    print(f'O maior valor passado foi {max(num)}.')

# Programa principal


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0, 7)
maior(1, 2)
maior(6)
maior(0)
print()