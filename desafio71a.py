print('*'*30)
print('{:^40}'.format('\033[1;31mBANCO MC.LOIOLA\033[m'))
print(('*'*30))
valor = int(input('Quanto deseja sacar? R$ '))
total = valor
ced = 100
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cedulas de R${ced}')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced ==20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        elif ced == 2:
            ced = 1
        totalced = 0
        if total == 0:
            break
print('*'*42)
print('\033[1;31mVOLTE SEMPRE ! O BANCO MC.LOIOLA AGRADECE\033[m')
