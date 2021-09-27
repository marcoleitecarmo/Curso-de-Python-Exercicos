from math import hypot
oposto = float(input('Informe o comprimento do cateto oposto: '))
adjacente = float(input('Informe o comprimento do cateto adjacente '))
hipotenusa = hypot(oposto, adjacente)
print('De acordo com o comprimento do cateto oposto {} e do cateto adjacente {}, o comprimento da hipotenusa é {:.2f} '.format(oposto, adjacente, hipotenusa))