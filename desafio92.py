from datetime import datetime

trabalhador = dict()
while True:
    trabalhador['Nome'] = str(input('Nome: ')). strip()
    nascimento = int(input('Ano de Nascimento: '))
    trabalhador['Idade'] = datetime.now().year - nascimento
    trabalhador['CTPS'] = int(input('Número da Carteira: (0 não tem) '))
    if trabalhador['CTPS'] == 0:
        trabalhador['CTPS'] = " Não tem Carteira "
        break
    else:
        trabalhador['Contratação'] = int(input('Ano da Contratação: '))
        trabalhador['Salário'] = float(input('Salario: R$ '))
        trabalhador['Aposentadoria'] = (trabalhador['Contratação'] - nascimento) + 35
        break
print('-' * 20)
for i, j in trabalhador.items():
    print(f'{i}: {j}')