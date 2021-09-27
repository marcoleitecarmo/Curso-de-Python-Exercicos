from random import sample
jogos = []
quant = int(input('Quantos jogos quer fazer? '))
for i in range(1, quant+1):
    jogos = [sample(range(1, 60), 6)]
    print(f'Jogo {i}: {jogos}')
    jogos.clear()

