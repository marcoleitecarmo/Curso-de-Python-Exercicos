aluno = {'Nome': str(input('Nome: ')).strip().upper(), 'Média': float(input('Média: '))}
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado(a)'
elif 6 <= aluno['Média'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado(a)'

for i, j in aluno.items():
    print(f'{i}: {j}')


