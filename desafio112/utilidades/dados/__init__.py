def leiaDinheiro(x):
    val = False
    while not val:
        entrada = str(input(x)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\33[1;31mERRO: \"{entrada}\" é um preço inválido!\33[m')
        else:
            val = True
            return float(entrada)
