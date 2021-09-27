cbf2021 = ('Atletico-MG', 'Palmeiras', 'Fortaleza', 'Bragantino', 'Flamengo',
           'Corinthian', 'Atletico-GO', 'Ceara','Athletico-PR', 'Internacional',
           'Santos', 'São Paulo', 'Fluminense', 'Juventude', 'Cuiaba', 'Bahia',
           'America-MG', 'Gremio', 'Sport Recife', 'Chapecoense')

op = int(input('''
[1] IMPRIMIR OS 5 PRIMEIROS COLOCADOS
[2] IMPIRMIR OS 4 ÚLTIMOS COLOCADOS
[3] IMPRIMIR OS TIMES EM ORDEM ALFABETICA
[4] IMPRIMIR A POSIÇÃO DO TIME DA CHAPECOENSE
 ESCOLA SUA OPÇÃO: '''))

if op == 1:
    for time in range(0, 5):
        print(f'{time+1}º{cbf2021[time]}')
elif op == 2:
    for time in range(16, 20):
        print(f'{time+1}º {cbf2021[time]}')
elif op == 3:
    print(f'Times em ordem alfabetica {sorted(cbf2021)}')
elif op == 4:
    print(f'Chapecoense esta na {cbf2021.index("Chapecoense")+1} posição.')
else:
    print('Opção Invalida!')



