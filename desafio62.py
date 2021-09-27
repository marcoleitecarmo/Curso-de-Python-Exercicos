from time import sleep

n = int(input('Digite primerio termo da P.A: '))
r = int(input('Digite a razão do P.A: '))

cpa = n
cont = 0
am = 10
total = 0

while am != 0:
    total = total + am

    while cont < total:
        print('{}-->'.format(cpa), end='')
        cpa = cpa + r
        cont += 1

    print('Pausa')
    sleep(1)

    am = int(input('''Desaja adicionar mais números: 
    [1] SIM
    [2] NÃO
    '''))

    if am == 1:
        am = int(input('Digite o número: '))

    if am == 2:
        break

print('Fim')
