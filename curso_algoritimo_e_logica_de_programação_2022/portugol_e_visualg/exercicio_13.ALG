Algoritmo "operadora"
// Disciplina   : [Linguagem e L?gica de Programa??o]
// Professor   : Antonio Carlos Nicolodi 
// Descri??o   : Aqui voc? descreve o que o programa faz! (fun??o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 31/08/2022
Var

   minuto : inteiro
   valor_base, valor_adicional, total : real

Inicio
   valor_base <- 50.00


   escreval("Digite a quantidade de minutos: ")
   leia(minuto)
   
   se (minuto > 100) entao
      valor_adicional <- (minuto - 100) * 2.00
      total <- valor_adicional + valor_base
      escreval("Valor a pagar : R$", total:6:2)
   senao:
      total <- valor_base
      escreval("Valor a pagar : R$", total:6:2)
   fimse
   
      
      



Fimalgoritmo