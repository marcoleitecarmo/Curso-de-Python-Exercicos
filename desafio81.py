n = list()
a = -1
while True:
    a += 1
    n.append(int(input('Digite um número: (0 para sair) ')))
    if n[a] == 0:
        n.pop()
        break
        a -= 1
n.sort(reverse=True)
print(f'''Números digitados: {a+1}
Valores  em ordem descrecente: {n}
O valor 5 foi digitado? Resposta: {'Sim' if 5 in n else 'Não'}''')




