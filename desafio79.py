lista = []
while True:
    num = int(input('Digite um número: '))
    if num in lista:
        print('O número ja esta  na lista.')
    else:
        lista.append(num)
        print('Número adicinado com sucesso...')
        opcao = str(input('Quer continuar sim ou não ? [S/N]')).strip().upper()[0]
        if opcao[0] == 'N':
            break
        elif opcao[0] == 'S':
            print(end='')
        else:
            print("Digite apenas 'S' ou 'N'!")
lista.sort()
print(f'Você digitou os seguintes números {lista}')
