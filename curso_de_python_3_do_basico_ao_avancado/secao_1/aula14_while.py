'''
while em python
Utilizado para realizar ações enquanto uma condição for verdadeira.

while condicao:
    pass
    continua = pula um bloco de codigo
    break = termina o loop
'''
# while False:
#     nome = input('Qual seu nome? ')
#     print(f'Ola {nome}!')


# x = 0 
# while x <= 100:
#     print(x)
#     x = x + 1

'''x = 0  #coluna
while x < 10:
    y = 0 #  linha

    while y < 5:
        print(f'({x} {y})')
        y += 1
    x += 1 # x = x + 1

print('Acabou')'''

'''
while/else
contadores acumuladores
'''
contador = 1
acumulador = 1

while contador < 10:
    print(contador, acumulador)

    acumulador = acumulador + contador
    contador += 1
else:
    print('Cheguei no else')




