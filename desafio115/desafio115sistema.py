from desafio115.lib.interface import *
from desafio115.lib.arquivo import *
from time import sleep

arquivo = 'cursodepython3.txt'
if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    resposta = menu(['Ver Cadastro', 'Cadastro', 'Sair'])
    if resposta == 1:
        lerArquivo(arquivo)
    elif resposta == 2:
        cabecalho('Novo Cadastro')
        nome = str(input('Digite o Nome: '))
        idade = leiaint('Digite a Idade: ')
        cadastar(arquivo, nome, idade)

    elif resposta == 3:
        print('Saindo....')
        break
    else:
        print('\033[31mErro!! Digite uma Opção válida!\033[m')
    sleep(2)
