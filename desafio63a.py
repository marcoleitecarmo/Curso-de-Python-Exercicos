termo = int(input('Quantos termos voê quer mostrar? '))
t1 = 1
t2 = 0
cont = 0
while cont < termo:
    soma = t1 + t2
    t1 = t2
    t2 = soma
    cont += 1
    print(soma, end=' -> ')
print('Fim')
