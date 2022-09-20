"""
- Criar variáveis para nome (str), idade (int), altura (float) e peso (float) de uma pessoa
- Criar variável com o ano atual (int)
- Obter o ano de nacimento da pessoa (baseado na idade e no ano atual)
- Obter o IMC da pessoa com casas decimais (pesdo e na altura da pessoa)
- Exibir um testo com todos os valores na rela usaond F-Strings (com as chaves)
"""

nome = 'keplin'
idade = 23
altura = 1.76
peso = 71.67
ano_atual = 2022
data_nasc = ano_atual - idade
imc = peso / (altura * altura)

print(f'Nome {nome}, idade {idade}, altura {altura}, peso {peso}, data de nascimento {data_nasc}, IMC {imc:.2f}')