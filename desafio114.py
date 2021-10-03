import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('Deu erro, Não consegui acessar o site pudim')
else:
    print('Deu certo Consegui acessar o site pudim')
    # print(site.read())
