import math
angulo = float(input('Informe o angulo '))
seno = math.sin(math.radians(angulo))
print('O angulo de {} tem o seno de {:.2f}' .format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O angulo de {} tem cosseno de {:.2f} '.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O angulo de {} tem a tangente de {:.2f} '. format(angulo, tangente))