"""
"""
'''usuario = input('Digite seu usuário: ')
qtd_caracteres = len(usuario)

print(usuario, qtd_caracteres, type(qtd_caracteres))

if  qtd_caracteres < 6:
    print('Você precisa digitar pelo menos 6 caracteres.')
else:
    print('Você foi cadastrado no sistema.')'''


string1 = input('Digite alguma coisa: ')
string2 = input('Digite outra coisa: ')

print(len(string1 + string2))


