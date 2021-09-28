def fatorial(num, show=False):
    fato = 1
    for i in range(num, 0, -1):
        fato *= i
    if show:
        for i in range(num, 0, -1):
            if i == 1:
                print('1', end=' ')
            else:
                print(i, end=' x ')
        print(f' = {fato}')
    else:
        print(f'Fatorial de {num}! é {fato}')


#  Programa Principal

numero = int(input('Digite o número para calcular o fatorial: '))
mostrar: int = int(input('Mostrar na tela? [0=Não/1=Sim] '))
fatorial(numero, mostrar)