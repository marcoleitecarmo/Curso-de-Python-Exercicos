from datetime import date

anoatual = date.today().year

ano = int(input('Digite o ano de nascimento: '))
idade = anoatual - ano
print('Quem nasceu em {} tem {} ano(s) de idade no ano de {}. '.format(ano, idade, anoatual))

if idade <= 9:
    print('Você pertence a categoria Mirim:')
elif idade <= 14:
    print('Você pertence a categoria Infantil:')
elif idade <= 19:
    print('Você pertence a categoria Junior:')
elif idade <= 25:
    print('Você pertence a categoria Senior:')
else:
    print('Você pertence a categoria Master!')
