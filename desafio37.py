num = int(input('Digite um número inteiro: '))
conv = int(input('Digite [1] para converter em binario \n'
                 'Digite [2] para converter em Octal \n'
                 'Digite [3] para converter em Hexadecimal \n'
                 'Digite uma das opções acima: '))


if conv == 1:
    conversao = bin(num)[2:]
elif conv == 2:
    conversao = oct(num)[2:]
elif conv == 3:
    conversao = hex(num)[2:]
else:
    print('Numero invalido !')

print('O numero {} convertido para conv {} é {} '.format(num, conv, conversao))

