from desafio108 import moedas

produto = float(input('Digite o preço do produto: R$ '))
print(f'A metade de {moedas.moeda(produto)} é {moedas.moeda(moedas.metade(produto))}')
print(f'O dobro de {moedas.moeda(produto)} é {moedas.moeda(moedas.dobro(produto))}')
print(f'Aumento com 10% temos {moedas.moeda(moedas.aumentar(produto, 10))}')
print(f'Reduzindo em 13% temos {moedas.moeda(moedas.diminuir(produto, 13))}')
