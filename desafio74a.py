from random import sample

num = tuple(sample(range(10), 5))
for i in num:
    print(i, end=' ')
print(f'''
Maior valor sorteado: {max(num)}
Menor valor sorteado: {min(num)}.''')