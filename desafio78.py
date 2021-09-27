valores = list()
for i in range(0, 5):
    valores.append(int(input(f'Digite um valor para a Posição {i}: ')))
print(f'Você digitou os valores {valores}')

print(f'\nMaior valor digitado: {max(valores)} posição: ', end=' ')
for i in range(0, 5):
    if valores[i] == max(valores):
        print(f'{i}...', end=' ')
print(f'\nMenor Valor digitado: {min(valores)} posição: ', end=' ')
for i in range(0, 5):
    if valores[i] == min(valores):
        print(f'{i}...', end=' ')
