soma = cont = 0
while True:
    n1 = int(input('Digite um número: [999 para sair] '))
    if n1 == 999:
        break
    cont += 1
    soma += n1
print(f'Você digitou {cont} valores e a soma entre eles é de {soma}')