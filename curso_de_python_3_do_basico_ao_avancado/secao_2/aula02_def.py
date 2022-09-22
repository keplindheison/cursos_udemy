"""
funções (def) - *args  - **kawargs

"""

'''from ssl import ALERT_DESCRIPTION_UNEXPECTED_MESSAGE


def func(a1, a2, a3, a4, a5):
    print(a1, a2, a3, a4, a5)

func(1,2,3,4,5)

def funcao(*args):
    print(args)
    print(args[0])
    print(args[-1])
    print(len(args))

funcao(1,2,3,4,5)

def func2(*args):
    for v in args:
        print(v)
func2('d', 6, 8, 'k', 'l')'''

def func3(*args, **kwargs):
    print(args)

    idade = kwargs['idade']

lista = [ 1,2,3,4,5]
lista2 = [10,20,30,40,50]
func3(*lista, *lista2, nome='Luiz', sobrenome='Miranda', idade=30)
