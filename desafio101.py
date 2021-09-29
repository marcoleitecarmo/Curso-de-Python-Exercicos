def voto(ano):
    from datetime import date
    data_atual = date.today().year
    idade = data_atual - ano
    if 18 <= idade <= 65:
        return f'Com {idade} anos: Voto Obrigatório'
    elif idade < 16:
        return f'Com {idade} anos: Voto Negado'
    else:
        return f'Com {idade} anos: Voto Opcional'


#  Programa Principal

data_Nascimento = int(input('Digite a data de Nascimento: '))
print(voto(data_Nascimento))