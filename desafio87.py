par = terc = maior = 0
matriz = [[[], [], []],
          [[], [], []],
          [[], [], []]]
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'[{i}][{j}] = '))
        if matriz[i][j] % 2 == 0:
            par += matriz[i][j]
        if j == 2:
            terc += matriz[i][j]
        if i == 1:
            maior = matriz[i][j]
print(matriz[0])
print(matriz[1])
print(matriz[2])
print(f'A soma de todos os valores pares é {par}')
print(f'A soma dos valores da terceira coluna é {terc}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')
print(f'O maior valor da segunda linha é {maior}')
