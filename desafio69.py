h = d18 = m = 0
while True:
    i = int(input('Digite a idade: '))
    s = a = ' '
    while s not in 'FM':
        s = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    if i > 18:
        d18 += 1
    if s in 'M':
        h += 1
    if s in 'F' and i < 20:
        m += 1
    while a not in 'SN':
        a = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if a == 'N':
        break
print(f'Pessoas com mais de 18 anos: {d18}')
print(f'Numero de homes cadastrados: {h}')
print(f'Mulheres com menos de 20 anos: {m}')

