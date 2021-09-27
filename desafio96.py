def linha(msg):
    print('-' * 30)
    print(f'{"|":<}{msg:^28}{"|":>}')
    print('-' * 30)


def area(larg, comp):
    ar = larg * comp
    print(f'A área de um terreno {larg:.1f} X {comp:.1f} é de {ar:.1f}m²')


# Programa Principal

linha('Calculo de área de um terreno')
la = float(input('Digite a Largura: '))
co = float(input('Digite o Comprimento: '))
linha("Resultado do Calculo")
area(la, co)
