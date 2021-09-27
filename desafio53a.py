pali = input('Digite uma Palavra: ').upper()
frasediv = pali.split()
frasejunta = ''.join(frasediv)
fraseinvertida = ''
for cont in range(len(frasejunta)-1, -1, -1):
    fraseinvertida += frasejunta[cont]
if fraseinvertida == frasejunta:
    print('Temos um Palindromo!')
else:
    print('A Frase digitada não é um Palindromo!')

print(f'Palavras junta: {frasejunta}')
print(f'Palavra invertida: {fraseinvertida}')
