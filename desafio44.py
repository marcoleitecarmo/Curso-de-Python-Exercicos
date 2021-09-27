print('{:=^40}'.format(' ATELIE AMOR E ALEGRIA '))
vp = float(input('\033[1;36mDigite o valor a ser pago pelo produto: R$ '))
print('\033[1;31mTemos algumas opções de pagamento: Escola a que estiver mais favaravél:')
print('\033[1;30mOpção [1] A vista no Dinheiro ou Cheque com 10% de desconto\n'
      '\033[1;30mOpçãp [2] A vista no cartão com 5 % de desconto\n'
      '\033[1;30mOpção [3] Em 2 X no cartão sai pelo preço normal\n'
      '\033[1;33mOpção [4] Em 3 X ou mais no cartão tem 20% de juros')
num = int(input('Digite a Opção desejada: '))
if num == 1:
    calc = vp - (vp * 10 / 100)
elif num == 2:
    calc = vp - (vp * 5 / 100)
elif num == 3:
    calc = vp
    parcela = vp / 2
    print('A sua compra sera parcelada em 2 X saindo com o valor de {}'.format(parcela))
    print('\n')
elif num == 4:
    calc = vp + (vp * 20 / 100)
    parcela = int(input('Em quantas parcelas deseja pagar? '))
    print('\n')
    np = calc / parcela
    print('Você escolheu em {} vezes logo cada parcela tem o valor de {:.2f}'.format(parcela, np))
else:
    calc = vp
    print('Opção Invalida de Pagamento. Tente Novamente!')
print('Você escolheu a Opção {}, o produto saira pelo valor de {}'.format(num, calc))
