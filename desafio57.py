sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]

while sexo not in 'MmFf':
    sexo = str(input('Dados Invalidos. Digite novamente! '))
print('Cadastrado com Sucesso! ')

