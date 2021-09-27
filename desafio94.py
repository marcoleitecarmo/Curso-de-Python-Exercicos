dicionario = dict()
lista = list()
mulheres = list()
soma = 0

while True:
    dicionario.clear()
    dicionario['Nome'] = str(input('Digite o nome: ')).strip()
    dicionario['Idade'] = int(input('Digite a idade: '))

    while True:
        dicionario['Sexo'] = str(input('Digite o sexo: [M/F]')).strip().upper()[0]
        if dicionario['Sexo'] in 'MF':
            break
        print('Opção Inválida! Tente novamente, desta vez com M ou F. ')

    lista.append(dicionario.copy())
    soma += dicionario['Idade']

    if dicionario['Sexo'] == 'F':
        mulheres.append(dicionario['Nome'])

    while True:
        opção = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if opção in 'SN':
            break
    if opção == 'N':
        break

print(f'A) Total de pessoa cadastradas: {len(lista)}')
print(f'B) A Média de idade: {soma/len(lista):.2f} anos')
print(f'C) Mulheres cadastradas: {mulheres}')
print(f'D) Pessoas com idade acima da média:')
for a in lista:
    if a['Idade'] >= soma/len(lista):
        print(f'   {a["Nome"]}: {a["Idade"]} anos ')

