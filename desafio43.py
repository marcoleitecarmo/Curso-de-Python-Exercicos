peso = float(input('Digite seu peso: (KG) '))
altura = float(input('Digite sua altura: (m) '))

imc = peso / (altura ** 2)
print('Com um peso de {} e uma altura de {} você tem um imc de {:.1f}'.format(peso, altura, imc))

if imc < 18.5:
    print('Você esta abaixo do peso! ')
elif imc <= 25:
    print('Você esta no peso ideal! ')
elif imc <= 30:
    print('Você esta com sobre Peso! ')
elif imc <= 40:
    print('Você esta com Obesidade! ')
elif imc > 40:
    print('Procure um médico urgente !!! Você esta com Obesidade Morbida')
