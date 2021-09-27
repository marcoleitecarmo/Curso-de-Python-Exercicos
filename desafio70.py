soma = c1000 = cont = menor = 0
nome = ' '
while True:
    cont += 1
    p = float(input('Preço do produto :R$  '))
    n = str(input('Nome do produto: ')).strip().capitalize()
    soma += p
    if p > 1000:
        c1000 += 1
    if cont == 1 or p < menor:
        menor = p
        nome = n
    c = ' '
    while c not in 'SN':
        c = str(input('Quer continua [S/N]')).strip().upper()[0]
    if c == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'Total das Compras: R$ {soma:.2f}')
print(f'Produto com preço acima de mil reais: {c1000}')
print(f'O produto mais barato é: {nome} e custa R$ {menor:.2f}')
