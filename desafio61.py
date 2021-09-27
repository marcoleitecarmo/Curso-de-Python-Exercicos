n = int(input('Digite um número: '))
r = int(input('Digite a razão do P.A: '))

termo = n
cont = 0
while cont < 10:
    print('{} --> '.format(termo), end='')
    termo = termo + r
    cont +=1

print('Fim')