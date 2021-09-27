n1 = int(input('Digite um número para fatorial: '))

cont = n1
fat = 1

while cont > 0:
    print('{}'.format(cont), end='')
    print(' X ' if cont > 1 else ' = ', end='')

    fat = fat * cont
    cont -= 1

print(fat)