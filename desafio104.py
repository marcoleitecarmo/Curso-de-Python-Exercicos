def leiaint(numero):
    while not numero.isnumeric():
        print(f' {numero} nã é um número valido')
        numero = input('Digite um número: ')
    return numero


#   Programa Principal

opcao = leiaint(input('Digite um número: '))
print(f'Você digitou o número {opcao}')
