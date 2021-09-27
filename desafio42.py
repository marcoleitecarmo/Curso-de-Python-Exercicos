la = float(input('Digite a medida da base a: '))
lb = float(input('Digite a medida da base b: '))
lc = float(input('digite a medida da base c: '))

if la < lb + lc and lb < la + lc and lc < la + lb:
    print('É um triângulo ', end='')
    if la == lb == lc:
      print('Equilátero:')
    elif la != lb != lc != la:
      print('Escaleno:')
    elif la == lb or lb == lc or la == lc:
      print('Isoceles:')
else:
    print('Os segmentos acima não podem formar um Triangulo')

