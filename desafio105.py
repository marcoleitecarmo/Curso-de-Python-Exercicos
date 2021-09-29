def notas(*n, s=False):
    """
    Dic[Notas]
    Função para categorizar dados(Notas) a serem informadas não importando a quantidade de dados [Notas]
    Returns:
            [dic['total']] -- [Retorna o valor total das notas]
            [dic['maior']] -- [Retorna o valor da maior nota]
            [dic['menor']] -- [Retorna o valor da menor nota]
            [dic['média']] -- [Retorna o valor da média das notas]
            [dic['situação']] -- [Retorna a situação do aluno]

    """

    dic = dict()
    dic['total'] = len(n)
    dic['maior'] = max(n)
    dic['menor'] = min(n)
    dic['média'] = (sum(n) / (dic['total']))

    while True:
        if dic['média'] >= 7:
            dic['situação'] = 'Boa'
        elif dic['média'] >= 5:
            dic['situação'] = 'Razoável'
        else:
            dic['situação'] = 'Ruim'
        return dic


# Programa Principal

print(notas(5.5, 9.5, 7, 5, 10, s=True))

help(notas)
