
#print(1234)
#print('Luiz', 'Otávio', 'Outra coisa')

print('Luiz', 'Otávio', sep='-', end='')  # mandando o argumento nomeado 'sep' e 'end'
print('João', 'e', 'Maria', sep='-')


"""
Exercicio rapido imprimir o seguinte cpf no formato abaixo:
824.176.070-18
"""

# Primeira forma
#print('824', '176', '070', sep='.', end='-')
#print(18)

'''
Segunda forma
print(824, end='.')
print(176, end='.')
print(870, end='-')
print(18)
'''
