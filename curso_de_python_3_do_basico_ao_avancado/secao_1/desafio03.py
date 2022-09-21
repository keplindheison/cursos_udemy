"""
Desafio validar um cpf:
CPF = 168.995.350-09
---------------------------------------------------------
1 * 10 = 10                 #   1 * 11 = 11 <-
6 * 9  = 54                 #   6 * 10 = 60
8 * 8  = 64                 #   8 *  9 = 72
9 * 7  = 63                 #   9 *  8 = 72
9 * 6  = 54                 #   9 *  7 = 63
5 * 5  = 25                 #   5 *  6 = 30
3 * 4  = 12                 #   3 *  5 = 15
5 * 3  = 15                 #   5 *  4 = 20
0 * 2  = 0                  #   0 *  3 =  0
                            #-> 0 *  2 =  0
        297                 #           343
11 - (297 % 11) = 11        #     11 - (343 % 11) = 9
11 > 9 = 0                  #
Digito 1 = 0                #   DIgito 2 = 9

"""

# Minha resolução do desafio
"""cpf_inserido = '168.995.350-09'

# formatando o cpf 
clear_cpf = []
for v in cpf_inserido:
    if v.isdigit():
        v = int(v)
        clear_cpf.append(v)


# numeros para a primeira conta
n_conta = []
for n in range(10, 1, -1):
    n = int(n)
    n_conta.append(n) 

#cpf limpo com -2 digitos
n_conta_cpf = list(clear_cpf)
while len(n_conta_cpf) >= 10: 
    del n_conta_cpf[-1]

#contas1
contador = 0
soma = []
while contador <= 8:
    soma.append(n_conta_cpf[contador] * n_conta[contador])
    contador += 1
if 11 - (sum(soma) % 11) > 9:
    n_conta_cpf.append(0)
else:
    n_conta_cpf.append(11 - (sum(soma) % 11))
  

#numeros para a segunda conta
n_conta = []
for n in range(11, 1, -1):
    n_conta.append(n) 
n_conta_cpf = list(clear_cpf)
#cpf limpo com -2 digitos
while len(n_conta_cpf) >= 11: 
    n_conta_cpf.pop()

#contas2
contador = 0
soma = []
while contador <= 9:
    soma.append(n_conta_cpf[contador] * n_conta[contador])
    contador += 1
if 11 - (sum(soma) % 11) > 9:
    n_conta_cpf.append(0)
else:
    n_conta_cpf.append(11 - (sum(soma) % 11))

if clear_cpf == n_conta_cpf:
    print(f'O CPF {n_conta_cpf} é valido.')
else:
    print(f'O CPF {n_conta_cpf} NÃO é valido.')"""





# Resolução do professor
cpf = '16899535009'
novo_cpf = cpf [:-2]

reverso = 10
total = 0

for index in range(19):
    if index > 8:
        index -= 9
    
    total += int(novo_cpf[index]) * reverso
    reverso -= 1
    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)

        if d > 9:
            d = 0
        total = 0
        novo_cpf += str(d)

print(novo_cpf)












