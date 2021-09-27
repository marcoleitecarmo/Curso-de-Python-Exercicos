soma = 0
contm = 0
media = 0
maior = 0
homemv = ''

for cont in range(1, 5):
    nome = str(input('Digite um nome: '))
    sexo = str(input('Masculino ou Feminino?[M/F]')).upper() [0]
    idade = int(input('Digite a idade: '))
    print('-'*20)

    soma = soma + idade
    media = soma / cont

    if sexo == 'M' and idade > maior:
        maior = idade
        homemv = nome

    if sexo == 'F' and idade < 20:
        contm += 1
print('Media das idades é de {:.2f}!'.format(media))
print('Nome do Homem mais velho é {}!'.format(homemv))
if contm == 0:
    print('Não temos mulher no grupo!')
else:
    print('Ao todo temo {} mulheres com menos de 20 anos: '.format(contm))
