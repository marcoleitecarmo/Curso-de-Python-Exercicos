print('=' * 30)
print('{:^40}'.format('\033[1;31mBANCO PYTHON\033[m'))
print('=' * 30)
valor = int(input('Qual o valor que deseja Sacar?R$ '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cedulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=' * 30)
print('\033[1;31mVolte Sempre ao BANCO PYTHON!\033[m ')
