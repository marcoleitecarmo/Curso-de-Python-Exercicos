num = list()
for c in range(0, 5):
    numeros = int(input('Digite um número: '))
    if c == 0 or numeros > num[-1]:
        num.append(numeros)
        print(f'o Valor {numeros} foi adicionado na ultima posição')
    else:
        p = 0
        while p < len(num):
            if numeros <= num[p]:
                num.insert(p, numeros)
                print(f'O valor {numeros} foi adicionado na posição {p}')
                break
            p += 1
print(f'Valores digitados: {num}')
