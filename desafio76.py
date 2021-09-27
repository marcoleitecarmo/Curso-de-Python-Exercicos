print('='*40)
print(f'{"LISTA DE PREÇOS":^40}')
print('='*40)
produtos = ('Açucar', 2.89,
            'Arroz 5 kg', 26.90,
            'Feijão', 6.89,
            'Café 500g', 14.89,
            'Farinha de Trigo', 3.29,
            'Oleo de Soja', 7.89,
            'Sal', 1.59,
            'Macarrão', 4.49,
            'Extrato de Tomate', 2.38,
            )
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R${produtos[pos]:>7.2f}')
print('='*40)
