soma = 0
cont = 0
for c in range(1, 7):
    n1 = int(input('Digite um numero: '))
    if n1 % 2 == 0:
        soma += n1
        cont += 1
print('Você informou {} numeros e a soma foi {} '.format(cont, soma))
