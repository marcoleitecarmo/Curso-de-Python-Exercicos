nome = str(input('Digite seu nome inteiro: ')).strip()
inteiro = nome.split()
print('Seu primeiro nome é {} '.format(inteiro[0]))
print('Seu ultimo nome é {} '.format(inteiro[len(inteiro)-1]))
