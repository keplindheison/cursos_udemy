"""
Tipos de dados
str - string - textos 'Assim' "Assim"
int - inteiro - 123456 0 -10 -20 -50 -60 -1500 1500
float - real/ponto flutuante - 10.50 1.5 -10.10 -50.93 0.0
bool - booleano/lógico - True/False 

"""

print('Luiz', type('Luiz'))  #função 'type()' retorna o tipo do dado 
print(10, type(10))
print(10.5, type(10.5))
print(True, type(True))

# Type cast - converter um tipo para outro
print('Luiz', type('Luiz'), bool('luiz'))
print('10', type('10'), type(int(10)))

# String: nome
print('Keplin', type('Keplin'))

# Idade: int
print(24, type(24))

# Altura: float
print(71.68, type(71.68))

# É maior de idade: >
print(24 > 18, type(24 > 18))