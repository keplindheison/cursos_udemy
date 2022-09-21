"""
For in em Python
Iterando strings com for
Função range(start=0, stop, step=1)
# continue - pula para o proximo laço
# break - termila o laço

"""
'''texto = 'Python'

for letra in texto:
    print(letra)

for n in range(10):
    print(n)

nova_string = ''

for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra  

print(nova_string)'''


'''
for / else
'''

variavel = ['Luiz Otávio', 'aoãozinho', 'Maria']

'''for valor in variavel:
    if valor.startswith('J'):
        print('COmeça com J', valor)
    else:
        print('Não começa com J', valor)'''

for valor in variavel:
    if valor.lower().startswith('j'):
        break
else:
    print('Não existe uma palavra que começa com J.')
