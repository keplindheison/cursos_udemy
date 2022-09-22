"""
1 - Crie um função1 que recebe uma função2 como parâmetro e retorne o valor da função2 executada.
"""
def func2():
    return 'hello'


def func(funcao):
    return funcao()


func = func(func2)
print(func)

"""
Crie uma função1 que recebe uma função2 como parametro e retorne o valor da função2 executada. Faça a função1 
executar duas funções que recebam um número diferente de argumentos.
"""

def func(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def func2(nome):
    return f'oOi {nome}'

def func3(nome, saudacao):
    return f'{saudacao} {nome}'

a = func(func2, 'Luiz')

print(a)
