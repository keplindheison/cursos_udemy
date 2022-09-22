"""
Funções - def
"""
#print('Hello World!')

'''def funcao():
    print('Heloo')

funcao()
funcao()
funcao()
funcao()


def saudacao(msg='Olá', nome='Usuário'):
    print(msg, nome)

saudacao('Olá', 'Luiz Otávio')
saudacao('Oi', 'Luiz')
saudacao('Hello', 'Maria')
saudacao('Olá', 'otávio')
saudacao('Olá', 'João')
saudacao()'''

from ssl import VERIFY_CRL_CHECK_LEAF


def funcao(var):
    return var

variavel = funcao('Valor que eu quero')

if variavel:
    print(variavel)
else:
    print('Nenhum valor.')


def divisao(n1, n2):
    if n2 == 0:
        return 
    return n1 / n2

divide = divisao(8, 0)
if divide:
    print(divide)
else:
    print('Conta inválida')


def dumb():
    return 1

print(type(dumb()))