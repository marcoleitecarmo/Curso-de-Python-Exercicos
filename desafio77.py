nomes = ('Alexandre', 'Mariane', 'Roberta', 'Fernanda', 'Marcelo')

for palavra in nomes:
    print(f'Palavra {palavra.upper()} \nVogais: ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
    print('\n')
