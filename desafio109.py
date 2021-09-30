from desafio109 import moedas

produto = float(input('Digite o preço do Produto: R$ '))
print(f'A metade de {moedas.moeda(produto)} é {moedas.metade(produto, True)}')
print(f'O dobro de {moedas.moeda(produto)} é {moedas.dobro(produto, True)}')
print(f'Aumentando em 10%, temos {moedas.aumentar(produto, 10, True)}')
print(f'Reduzindo em 13%, temos {moedas.diminuir(produto, 13, True)}')

