"""
1 - Crie uma função que exibe uma saudação com os parâmetros saudação e nome.
"""

def sauda(saudacao, nome):
    return(saudacao, nome)

#print(sauda('hello', 'pessoa'))

"""
2 - Crie uma função que recebe 3 números como parâmetros e exiba a soma entre eles.
"""

def soma(n1, n2, n3):
    return n1 + n2 + n3

print(soma(5, 4, 3))

"""
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um percentual (ex. 10%). retorne (return)
o valor do primeiro número somado do aumento do percentual do mesmo.
"""

def aumento(valor, percentual):
    return valor + (valor * percentual / 100)

print(aumento(100, 50))
    

"""
4 - fizz buzz - se o prarâmetro da função for divisivel por 2, retorne fizz, se o parametro da função for divisivel 
por 5. retorne buzz. se o parametro da função for divisivel por 5 e por 3, retorne FIZZBUZZ, caso contrario, retorne 
o numero é invalido 
"""

def fb(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    if n % 3 == 0:
        return 'Buzz'
    if n % 5 == 0:
        return 'fizz'
    return 'Numero invalido'

print(fb(10))
print(fb(15))
print(fb(1))