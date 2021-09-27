dist = float(input('Informe a distância da viagem '))
if dist <= 200:
    print('O preço da passagem é R${:.2f} '.format(dist*0.50))
else:
    print('O preço da passagem é R${:.2f} '.format(dist*0.45))
    

