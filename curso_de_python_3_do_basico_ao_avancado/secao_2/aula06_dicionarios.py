"""
dicionario - chave - valor
"""

d1 = {'chave1': 'valor da chave'}
d1['Nova_chave'] = 'calor da nova chave'

#print(d1)
#print(d1['chave1'])

d2 = dict(chave1='valor da chave', chave2='valor da outra chave')
#print(d2)

d3 = {
    'str' : 'valor',
    123 : 'Outro valor',
    (1,2,3,4) : 'Tupla',
}

'''print(d3[(1,2,3,4)])
print(d3.keys())
print(d3.values())
print('valor' in d3.values())
print(len(d3))'''

#for k in d3.items():
    #print(k)

clientes = {
    'cliente1' : {
        'nome' : 'Luiz',
        'sobrenome' : 'otavio'
    },
    'cliente2' : {
        'nome' : 'Joao',
        'sobrenome' : 'momeira'
    },
}


for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'{dados_k} = {dados_v}')