n1 = int(input('Digite o primeiro termo da P.A '))
razao = int(input('Digite a Razão da P.A '))

decimo = n1 + (10 - 1) * razao
for c in range(n1, decimo + razao, razao):
    formula = n1 + razao
    print(c, end='--->')
print()
print('Fim')
