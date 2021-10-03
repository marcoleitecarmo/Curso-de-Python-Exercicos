def leiaint():
    while True:
        try:
            n = int(input('Digite um número inteiro: '))
        except (ValueError, TypeError):
            print('\033[31mErro! Por favor digite um número inteiro válido\033[m')
            continue
        else:
            return n


def leiafloat():
    while True:
        try:
            n = float(input('Digite um número real: '))
        except (ValueError, TypeError):
            print('\033[31mErro! Por favor digite um número real válido\033[m')
            continue
        else:
            return n


num1 = leiaint()
num2 = leiafloat()

print('-' * 20)
print(f'Número Inteiro: {num1}')
print(f'Número Real: {num2}')
print('-' * 20)
