Algoritmo "exercicio_03"

//Problema "retangulo"
//Fazer um programa para ler as medidas da base e altura de um retângulo. Em seguida, mostrar o valor
//da área, perímetro e diagonal deste retângulo, com quatro casas decimais, conforme exemplos. 


Var
   base, altura, area, perimetro, diagonal : real
Inicio
      escreva("Base do retangulo: ")
      leia(base)
      escreva("Altura do retangulo: ")
      leia(altura)
      
      area <- base * altura
      perimetro <- 2 * (base + altura)
      diagonal <- RaizQ(Exp(base, 2) + Exp(altura, 2))
      
      escreval("Area = ", area)
      escreval("Perimetro = ", perimetro)
      escreval("Diagonal = ", diagonal)

Fimalgoritmo