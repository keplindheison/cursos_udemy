'''
https://docs.python.org/3/library/stdtypes.html
'''

num1 = input('Digite um número: ')
num2 = input('Outro número: ')

# isnumeric isdigit isdecimal -> numeros positivos e inteiros 

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    print(num1 + num2)
else:
    print('Não pode converter os números para realizar contas.')






