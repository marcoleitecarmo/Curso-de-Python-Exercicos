nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2
print('A soma da primeira nota {} com a segunda nota {} deu à seguinte média {:.1f}'.format(nota1, nota2, media))

if media < 5:
    print('\033[1;31mVocê foi reprovado!')
elif 7 > media >= 5:
    print('\033[1;33mVocê esta de recuperação..')
else:
    print('\033[1;34mParabéns você foi aprovado!!!!')

