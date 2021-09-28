def func(ajuda):
    print('\033[7m-' * 30)
    help(ajuda)
    print('\033[m-' * 30)


while True:
    print('\033[41m-' * 30)
    print(f'{"Sistema de ajuda PyHelp":^30}')
    print('-' * 30)

    opc = (str(input('Função ou Biblioteca (Fim para sair) ->')))
    if opc == 'Fim':
        break

    func(opc)
