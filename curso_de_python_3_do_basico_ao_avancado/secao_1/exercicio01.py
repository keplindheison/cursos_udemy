'''
Faça um programa que peça ao usuário para digitar um número inteiro,
informa se este número é par ou ímpar. Caso o usuário não digite um número 
inteiro, informa que não é um número inteiro.

'''


#  num = input('Digite um número: ')

#  if num.isdigit():
#      num = int(num)
#      if num % 2 == 0:
#          print('O número digitado é par.')
#      else:
#          print('O número digitado é impar')
#  else:
#      print('O número digitado não é um número inteiro!')

'''
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
'''
# hora = input('Digite a hora')

# if hora.isdigit():
#     hora = int(hora)
#     if hora > 0 and hora <= 11:
#         print('Bom dia')
#     elif hora > 11 and hora <= 17:
#         print('Boa Tarde')
#     else:
#         print('Boa noite')
# else:
#     print('Digite um horario valido!')


'''
Faça um programa que peça o primeiro nome do usuário . Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal". maior que 6 escreva "Seu nome é muito grande". 
'''

nome = input('Digite o seu primeiro nome')

if len(nome) <=4:
    print('Seu nome é curto')
elif len(nome) <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é grande')