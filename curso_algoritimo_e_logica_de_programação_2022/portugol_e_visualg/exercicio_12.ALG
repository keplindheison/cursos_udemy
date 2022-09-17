Algoritmo "menor_de_tres"
//Problema "menor_de_tres"
//Fazer um programa para ler três números inteiros. Em seguida, mostrar qual o menor dentre os três
//números lidos. Em caso de empate, mostrar apenas uma vez. 



Var

   n1, n2, n3 : inteiro


Inicio

   escreval("Primeiro valor: ")
   leia(n1)
   escreval("Segundo valor: ")
   leia(n2)
   escreval("Terceiro valor: ")
   leia(n3)
   
   se (n1 < n2) e (n1 < n3)entao
      escreval("MENOR =" , n1)
   senao
      se (n2 < n1) e (n2 < n3)entao
         escreval("Menor = ", N2)
      sen�o
         escreval("Menor = ", n3)
      fimse
   fimse

Fimalgoritmo