exp = str(input('Digite uma expressão: '))
if exp.count('(') == exp.count(')'):
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
