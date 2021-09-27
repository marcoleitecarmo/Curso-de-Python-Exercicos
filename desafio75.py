num = (int(input('1ªValor: ')), int(input('2ªValor: ')), int(input('3ªValor: ')), int(input('4ªValor: ')))
print(num)
print(f'O número 9 aparece {num.count(9)} vezes.')
if 3 in num:
    print(f'O número 3 foi digitado pela primeira vez na  posição {num.index(3)+1}')
else:
    print('O numero 3 não foi digitado.')
print('Os números pares digitados foram: ', end=' ')
for i in num:
    if i % 2 == 0:
        print(f'{i} ', end=' ')


