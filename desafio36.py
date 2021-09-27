imovel = float(input('Digite o valor do imovél: '))
salário = float(input('Digite o valor do salário: '))
anos = float(input('Digite em quantos anos quer pargar: '))

parcelas = anos * 12
prestação = imovel / parcelas
print('Para pagar o imovél de R$ {:.2f} em {} anos as parcelas serão de R$ {:.2f} '.format(imovel, anos, prestação))

if prestação < 30 / 100 * salário:
    print('Emprestimo Aprovado')
else:
    print('Emprestimo Negado !')


