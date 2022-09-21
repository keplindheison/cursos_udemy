"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
#         0    1    2    3    4
'''lista = ['A', 'Bacana', 'C', 'D', 'E', 10.5]
# -      -5   -4   -3   -2   -1

string = 'ABacanaCDE'
print(string[1])
print(lista[-1])

# modificar um item da lista
lista[5] = 'Qualquer outra coisa'
print(lista)

# mostrando algus elementos da lista
print(lista[::2])
print(lista[0:3])
'''

l1 = [1,2,3]
l2 = [4,5,6]
l3 = l1 + l2

print(l1)
print(l2)
print(l3)

# append - inseri um valor na ultima posição da lista
l2.append('b')

print(l2)

# insert - inseri um valor no indice que vc especificar
l2.insert(0, 'banana')
print(l2)


# pop - deleta o ultimo item da lista
l2.pop()
print(l2)

l2 = [1,2,3,4,5,6,7,8,9]
print(l2)

# del - exceluir elementos expecificando o indice
del(l2[3:5])
print(l2)

# max - pegar o maior valor da lista
print(max(l2))
# min - pegar o menor valor da lista
print(min(l2))


l3 = list(range(1,10))
print(l3)

soma = 0
for valor in l2:
    soma = soma + valor

print(soma)

l4 = ['String', True, 10, -20.5]

for elemento in l4:
    print(f'O tipo de elemento é {type(elemento)} e seu valor é {elemento}')


secreto = 'perfume'
digitada = []
chances = 3

while True:
    if chances <= 0:
        print('Voce perdeu')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Ahh isso não vale, digite apenas uma letra.')
        continue
    digitada.append(letra)
    if letra in secreto:
        print(f'a letra {letra}, existe na palavra secrata.')
    else:
        print(f' a letra {letra} nao existe na palavra secreta.')
        digitada.pop()
    secreto_temporario =''
    for letra_secreta in secreto:
        if letra_secreta in digitada:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
    
    if secreto_temporario == secreto:
        print('Voce ganhou')
        break
    else:
        print(f'A palavra secreta esta assim: {secreto_temporario}')
    
    if letra not in secreto:
        chances -= 1

    print(f'Voce ainda tem {chances} chances.')