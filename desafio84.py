lista = []
pessoas = []
maior = menor = 0
while True:
    lista.append(str(input('Digite o nome: ')))
    lista.append(float(input('Digite o peso: ')))
    if len(pessoas) == 0:
        maior = menor = lista[1]
    else:
        if lista[1] > maior:
            maior = lista[1]
        if lista[1] < menor:
            menor = lista[1]
    pessoas.append(lista[:])
    lista.clear()
    opção = str(input('Quer continuar? [S/N ]')).strip().upper()[0]
    if opção == 'N':
        break
print(f'Quantidade: {len(pessoas)}')
print(f'Maior Peso {maior}')
print(f'Menor Peso {menor}')
