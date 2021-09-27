sal = float(input('Digite seu salario atual R$ '))
ns = sal + (sal*15/100)
print('Seu salario atual é de R$ {:.2f} com o reajuste será de R$ {:.2f} '.format(sal, ns))
