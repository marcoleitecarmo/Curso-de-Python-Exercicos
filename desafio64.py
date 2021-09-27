n = soma = cont = 0
while True:
    num = int(input('Digite um número: [999 para Finalizar]: '))
    if num != 999:
        soma += num
        cont += 1
    else:
        break
print('\033[1;31mSaiu do loop\033[m', '\n')
print('\033[1;32mForam digitados ao todo {} numeros e a soma dos valoes é {}\033[m'.format(cont, soma))