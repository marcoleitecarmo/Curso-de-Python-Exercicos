jogador = dict()
gols = list()

jogador['Nome']= str(input('Nome do jogador: ')).strip()
partidas = int(input(f' Quantas Partidas {jogador["Nome"]} jogou? '))
if partidas > 0:
    for c in range(0,  partidas):
        gols.append(int(input(f' Quantos gols na {c+1}º partidas? ')))
    jogador['Gols'] = gols[:]
    jogador['Total'] = sum(gols)
print('-=' * 40)
print(jogador)

print('-=' * 40)
for i, j in jogador.items():
    print(f'{i}: {j}')

print('-=' * 40)
print(f'O Jogador {jogador["Nome"]} jogou {partidas} partidas')
for i, j in enumerate(gols):
    print(f'        Na {i+1}º partida fez {j} gols')
print(f'Foi um total de {jogador["Total"]} gols')
