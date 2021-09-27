termo = int(input('Digite quntos você quer mostrar? '))
a = 1
b = 0
aux = 1
cont = 0
print('1', end='')

while cont < termo:
    aux = a
    a = a + b
    b = aux
    print(' --> ', a, end='')
    cont += 1
print()

