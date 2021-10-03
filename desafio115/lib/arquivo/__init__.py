from desafio115.lib.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Erro na Criação do Arquivo!')
    else:
        print(f'Arquivo {nome} criado com Sucesso!')


def lerArquivo(nome):
    global a
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler Arquivo')
    else:
        cabecalho('Cadastro')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:.3} anos')
    finally:
        a.close()


def cadastar(arquivo, nome='desconhecido', idade=0):
    try:
        a = open(arquivo, 'at')
    except:
        print('Erro na Abertura do Arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Erro ao digitar os dados!')
        else:
            print(f'Registrado com Sucesso {nome}')
            a.close()
