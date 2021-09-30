def moeda(x):
    return f'R$ {x:.0f},00'


def aumentar(x, a, f=False):
    m = x + ((a * x) / 100)
    return m if f is False else moeda(m)


def diminuir(x, d, f=False):
    n = x - ((d * x) / 100)
    return n if f is False else moeda(n)


def dobro(x, f=False):
    d = x * 2
    return d if f is False else moeda(d)


def metade(x, f=False):
    m = x / 2
    return m if f is False else moeda(m)


def resumo(x, p=10, g=5):
    print('\033[c')
    print('-' * 30)
    print(f"{'|'}{'Resumo do Preço'.center(28)}{'|'}")
    print('-' * 30)
    print(f'''Analizado Preço:          \t{moeda(x)}
Dobro do Preço:           \t{dobro(x, True)}
Metade do Preço:          \t{metade(x, True)}
{p}% porcento de aumento: \t{aumentar(x, p, True)}
{g}% porcento de desconto: \t{diminuir(x, g, True)}
''')
    print('-' * 30)
    print()
