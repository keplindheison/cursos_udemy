"""
"""


l1 = [1,2,3,4,5,6,7,8,9]
l2 = [variavel for variavel in l1]
l3 = [v * 2 for v in l1]
l4 = [(v, v2) for v in l1 for v2 in range(3)]


l5 = ['Luiz', 'Mauro', 'Maria']
l6 = [v.replace('a', '@') for v in l5]

tupla = (
    ('Chave', 'valor'),
    ('Chave2', 'valor2')
)

tupla2 = [(y, x) for x, y in tupla]

print(tupla2)

l7 = list(range(100))
l8 = [v for v in l7 if v % 2 == 0]
print(l8)