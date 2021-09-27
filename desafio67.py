print('*' * 30)
print('     Monte sua Tabuada:   ')
print('*' * 30)
while True:
    tab = int(input('Digite um número para criar a tabuada: '))
    if tab < 0:
        print('Programa Encerrado!')
        break

    for c in range(1, 11):
        print(f'{tab} X {c} = {tab * c}')
