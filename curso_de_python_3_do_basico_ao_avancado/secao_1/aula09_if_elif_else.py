"""
Condições IF, ELIF, ELSE

"""

# Booleanos
'''if True:
    print('Verdadeito')

    num1 = 2
    num2 = 4

    print(num1 + num2)'''

"""if False:
    print('Verdadeiro')
else:
    print('A minha expressão não é verdadeira')"""

'''if False:
    print('verdadeiro')
elif True:
    print('Agora é verdadeiro')
else:
    print('Não é verdadeiro')'''

# Operadores Relacionais
# ==, >, >=, <, <=, !=

'''


nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))

#Limite para pegar o empréstimo
idade_menor = 18 #  muito jovem 
idade_maior = 30 #  muito velho

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o emprestimo.')
else:
    print(f'{nome} NÂO pode pegar o emprestimo.')
'''

'''
Operadores Lógicos 
and, or, not
in e not in
'''

a = 2
b = 2
c = 3


a == b and b < c

a == b or b < c

usuario = input('Nome de usuário: ')
senha= input('Senha do usuário: ')

usuario_bd = 'keplin'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Login efetuado com sucesso')
else:
    print('Senha ou Usuário invelido')










