lista = list()
par = list()
impar = list()
while True:
    lista.append(int(input('Digite um número: (0 para sair)')))
    if lista[-1] == 0:
        lista.pop()
        break
    if lista[-1] % 2 == 0:
        par.append(lista[-1])
    else:
        impar.append(lista[-1])
lista.sort()
print(f'Valores da lista: {lista}')
print(f'Valores par: {par}')
print(f'Valores impar: {impar}')
