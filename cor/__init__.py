def cor_print(c, txt):
    cor = {'vermelho': '\33[1;31m',
           'verde': '\33[1;32m',
           'amarelo': '\33[1;33m',
           'azul': '\33[1;34m',
           'roxo': '\33[1;35m',
           'azul claro': '\33[1;36m',
           'cinza': '\33[1;37m',
           'sem cor': '\33[m'
           }
    print(cor[c])
    print(txt, end='')
    print(cor['sem cor'])


def cor_ret(msg):
    cor = {'vermelho': '\33[1;31m',
           'verde': '\33[1;32m',
           'amarelo': '\33[1;33m',
           'azul': '\33[1;34m',
           'roxo': '\33[1;35m',
           'azul claro': '\33[1;36m',
           'cinza': '\33[1;37m',
           'sem cor': '\33[m'
           }
    return cor[msg]
