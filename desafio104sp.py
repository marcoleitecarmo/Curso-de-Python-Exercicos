def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        a = str(input(msg))
        if a.isnumeric():
            valor = int(a)
            ok = True
        else:
            print('\033[0;31mErro! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor

# Programa Principal


a = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {a}')
