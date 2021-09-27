from datetime import date
anoatual = date.today().year

ano = int(input('Informe seu ano de nascimento: '))

idade = anoatual - ano
print('Quem nasceu em {} tem {} anos, no ano de {}.'.format(ano, idade, anoatual))

if idade < 18:
    print('Você ira se alistar em {} ano(s)'.format(18 - idade))
elif idade == 18:
    print('Você ira se alistar nesse ano de {}.'.format(anoatual))
elif idade > 18:
    print('Você deveria ter se alistado há {} anos'.format(idade-18))
    print('Seu alistamento foi em {}:'.format(anoatual-(idade - 18)))

