pali = input('Digite uma palavra. ').upper().replace('','')
if pali == pali[:: -1]:
    print('A palavra é palindroma.!''\n')
    print('A Palavra Invertida: {}'.format(pali),'\n')
else:
    print('A palavra não é palindroma!''\n')
print('A palavra digitada: {}'.format(pali), '\n')
