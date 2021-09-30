from desafio107 import moedas

produto = float(input('Digite o preço do produto: R$ '))
print(f'A metade de R$ {produto} é R$ {moedas.metade(produto)}')
print(f'O dobro de R$ {produto} é R$ {moedas.dobro(produto)}')
print(f'Aumento de 10%, temos R$ {moedas.aumentar(produto, 10)}')
print(f'Reduzindo em 13%, temos R$ {moedas.diminuir(produto, 13)}')

