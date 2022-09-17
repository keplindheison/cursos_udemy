# Estrutura repetitiva enquanto (while)

soma = 0 
x = int(input("Digite o primeiro numero: "))

while x != 0:
    soma = soma + x
    x = int(input("Digite outro numer: "))

print(f"Soma = {soma}")