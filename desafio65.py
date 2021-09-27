soma = cont = media = maior = menor = 0
resp = ''
while resp != 'N':
    n1 = int(input('Digite um numero: '))
    resp = input('Quer Continuar [S/N]').upper().strip()[0]
    soma = soma + n1
    cont += 1
    media = soma / cont
    if cont == 1:
        maior = menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1
print('\033[1;31mVocê digitou {} numeros e a soma entre eles é {}\033[m'.format(cont, soma))
print('\033[1;32mA média entre eles é {:.2f}\033[m'.format(media))
print('\033[1;33mO maior número é {} e o menor número é {}\033[m'.format(maior, menor))
