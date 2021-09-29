def leiaint(numero):
    while not numero.isnumeric():
        print(f' {numero} não é um número valido')
        numero = input('Digite um número: ')
    return numero


#   Programa Principal

opc = leiaint(input('Digite um número: '))
print(f'Você digitou o número {opc}')
