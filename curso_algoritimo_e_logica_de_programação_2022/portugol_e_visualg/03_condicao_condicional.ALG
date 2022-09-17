Algoritmo "condicao_condicional"

Var
   hora : inteiro

Inicio
   escreva("Digite uma hora do dia: ")
   leia(hora)
   
   se hora < 12 entao
      escreva("Bom dia")
   senao
      se hora < 18 entao
         escreva("Boa tarde")
      senao
         escreval ("Boa noite")
      fimse
    fimse

Fimalgoritmo