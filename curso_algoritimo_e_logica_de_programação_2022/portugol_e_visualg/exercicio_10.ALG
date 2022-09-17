Algoritmo "exercicio_10"
//Fazer um programa para ler as duas notas que um aluno obteve no primeiro e segundo semestres de
//uma disciplina anual. Em seguida, mostrar a nota final que o aluno obteve (com uma casa decimal) no
//ano juntamente com um texto explicativo. Caso a nota final do aluno seja inferior a 60.00, mostrar a
//mensagem "REPROVADO", conforme exemplos. 



VAR
        nota1, nota2, media : real
Inicio
        escreval("Digite a primeira nota: ")
        leia(nota1)
        escreval("Digite a segunda nota: ")
        leia(nota2)
        
        media <- (nota1 + nota2) / 2
        
        se media >= 60.00 entao
           escreval("Nota Final = ", media:5:1)
        senao:
           escreval("Nota final = ", media:5:1)
           escreval("Reprovado")
        fimse


Fimalgoritmo