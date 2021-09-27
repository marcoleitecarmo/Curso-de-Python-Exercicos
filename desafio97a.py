def frase(msg):
    tam = len(msg) + 4
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)


# Programa Principal

texto = str(input('Digite uma frase: '))
frase(texto)
