from datetime import date
anoatual = date.today().year
ano = 0
maioridade = 0
menoridade = 0
for c in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idadepessoa = anoatual - ano
    if idadepessoa >= 21:
        maioridade += 1
    else:
        menoridade += 1

print('Maiores idades {} '.format(maioridade))
print('Menores idades {} '.format(menoridade))
