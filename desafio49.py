num = int(input('Digite o número que você quer criar uma tabuada '))
for c in range(0,11):
    print('{} X {} = {} '.format(num, c, (num * c)))
