n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

while True:
    opcao = int(input('''\033[1;31mEscolha uma opção: 
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] NÚMERO AO QUADRADO
    [6] SAIR DO PROGRAMA\033[m
    \n'''))

    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {:.0f} e {:0f} a soma é {:.0f}'.format(n1, n2, soma))

    elif opcao == 2:
        multiplicar = n1 * n2
        print('A mutiplicação de {:.0f} e {:.0f} é {:.0f}'.format(n1, n2, multiplicar))

    elif opcao == 3:
        if n1 > n2:
            print('O maior número é {}'.format(n1))
        else:
            print('O maior número é {}'.format(n2))

    elif opcao == 4:
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))

    elif opcao == 5:
        resultado = int(input('Qual número deseja elevar ao quadrado? '))
        if resultado == n1:
            quadrado = resultado * resultado
            print('O número {} ao quadrado é {}'.format(n1, quadrado))
        elif resultado == n2:
            quadrado = resultado * resultado
            print('O número {} ao quadrado é {}'.format(n2, quadrado))
    elif opcao == 6:
        break
            
