Algoritmo "semnome"
//Faça um programa para ler um número indeterminado de dados, contendo cada um, a idade de um
//indivíduo. O último dado, que não entrará nos cálculos, contém um valor de idade negativa. Calcular
//e imprimir a idade média deste grupo de indivíduos. Se for entrado um valor negativo na primeira vez,
//mostrar a mensagem "IMPOSSIVEL CALCULAR".


Var

   idade, contador, soma : inteiro
   media : real

Inicio


   escreval("Digite as idades: ")
   leia(idade)

   contador <- 1
   soma <- idade

   se idade < 0 entao
      escreval("Imposilvel calcular")
   fimse
   
   enquanto idade > 0 faca
      leia(idade)
      se idade > 0 entao
         contador <- contador + 1
         soma <- soma + idade
      fimse
   fimenquanto
   
   media <- soma / contador
   se media > 0 entao
      escreval("media = ", media)
   fimse

      


Fimalgoritmo