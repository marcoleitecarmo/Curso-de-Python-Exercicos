print('\33c')
exp = str(input('Digite sua expressão: '))
lista = list()
for simb in exp:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Expressão valida !')
else:
    print('Expressão invalida..')