def fatorial(num, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param num: O número a ser calculado
    :param show: (opcional) Mostra ou não a conta
    :return: O Valor do Fatorial do número
    """

    f = 1
    for i in range(num, 0, -1):
        f *= i
    if show:
        for i in range(num, 0, -1):
            if i == 1:
                print('1', end=' ')
            else:
                print(i, end=' x ')
        print(f' = {f}')
    else:
        print(f'Fatorial de {num}! é {f}')


#  Programa Principal

numero = int(input('Digite o número para calcular o fatorial: '))
mostrar = int(input('Mostrar na tela? [0=Não/1=Sim] '))
fatorial(numero, mostrar)

# help(fatorial)
