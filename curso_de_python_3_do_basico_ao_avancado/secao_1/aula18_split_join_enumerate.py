"""
Split, Join, Enumerate
* Split - Dividir uma string # str
* Join - Juntar uma lista # str
* Enumerate - enumerar elementos da lista # list
"""
'''string = 'O Brasil é o pais do futebol, o Brasil é penta.'
lista = string.split(' ')
lista2 = string.split(',')

print(string)
print(lista)
print(lista2)

for valor in lista2:
    print(valor)'''


'''string = 'O Brasil é o pais do futebol, o Brasil é penta.'
lista = string.split(' ')
string2 = ' '.join(lista)

print(string2)'''

'''string = 'O Brasil é o pais do futebol, o Brasil é penta.'
lista = string.split(' ')

for indice, valor in enumerate(lista):
    print(indice, valor)'''

lista = [
        [1,2],
        [3,4],
        [5,6],
]


for v in lista:
    #print(v)
    print(v[0], v[1])


