dias = int(input("Qauntos dias Alugados? "))
km = float(input('Quanots Km rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R$ {:.2f}'.format(pago))
