"""
Escopo de variaveis
"""

variavel = 'valor'  #variavel global

def func():
    print(variavel)

def func2():
    variavel = 'Outro valor'
    print(variavel)


func()
func2()

print(variavel)

def func3():
    global variavel
    variavel = 'Outro valor'
    print(variavel)

func3()
print(variavel)