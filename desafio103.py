def ficha(nome='desconhecido', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')

# Programa Principal


jogador = str(input('Digite o nome do jogador: '))
gol = str(input('Digite o número de gols: '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if jogador.strip() == '':
    ficha(gols=gol)
else:
    ficha(jogador, gol)
