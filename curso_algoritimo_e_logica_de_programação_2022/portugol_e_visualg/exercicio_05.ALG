Algoritmo "exercicio_05"

//Problema "idades"
//Fazer um programa para ler o nome e idade de duas pessoas. Ao final mostrar uma mensagem com os
//nomes e a idade média entre essas pessoas, com uma casa decimal, conforme exemplo. 

Var

   nome1, nome2 : caractere
   idade1, idade2 : inteiro
   media : real

Inicio
   escreval("Digite o primeiro nome: ")
   leia(nome1)
   escreval("Digite a primeira idade: ")
   leia(idade1)
   
   escreval("Digite o segundo nome: ")
   leia(nome2)
   escreval("Digite a segunda idade: ")
   leia(idade2)
   
   media <- (idade1 + idade2) / 2
   
   escreval("A idade m�dia de ", nome1, " e ", nome2, " � de ", media, " anos" )
   


Fimalgoritmo