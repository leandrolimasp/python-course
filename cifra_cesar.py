#ord() retorna código da string
#chr() retorna string do código

def esconde(msg):
    s = ''
    for c in msg: s += chr(ord(c) + 3000)
    return s

def mostra(msg):
    s = ''
    for c in msg: s += chr(ord(c) - 3000)
    return s

'''
no terminal acessar o dir do arquivo:
python3
from cifra_cesar import*
esconde('qualquer coisa')
mostra('coloca aqui a criptografia')
'''

