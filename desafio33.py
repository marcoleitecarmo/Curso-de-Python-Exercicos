n1 = int(input('Digite o Primeiro numero '))
n2 = int(input('Digite o Segundo numero '))
n3 = int(input('Digite o Terceiro numero '))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O menor numero foi {} '.format(menor))
print('O maior numero foi {} '.format(maior))




