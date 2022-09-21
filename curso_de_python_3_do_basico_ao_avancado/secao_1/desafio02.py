'''
Desafio conseguir mostrar a sequencia abaixo:
for / while
0 10
1 9
2 8
3 7
4 6
5 5
6 4
7 3
8 2
'''
# Minha resolução
lista = []
for n in range(10, 1, -1): 
    lista.append(n)
for n1, n2 in enumerate(lista):
    print(n1, n2)


# Resolução do professor


for p, r in enumerate(range(10, 1, -1)):
    print(p, r)