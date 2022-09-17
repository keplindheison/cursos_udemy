Algoritmo "execico_08"
// Problema "pagamento"
//Fazer um programa para ler o nome de um(a) funcionário(a), o valor que
//ele(a) recebe por hora, e a quantidade de horas trabalhadas por ele(a). Ao final, mostrar o valor do
//pagamento do funcionário com uma mensagem explicativa, conforme exemplo

Var

   nome: caractere
   valor_h : real
   hora_t : inteiro
   pagamento: real


Inicio
      escreval("Digite seu nome: ")
      leia(nome)
      escreval("Valor da hora: ")
      leia(valor_h)
      escreval("Quantidade de horas trabalhadas: ")
      leia(hora_t)
      
      pagamento <- valor_h * hora_t
      
      escreval("O pagamento para ", nome, " deve ser ", pagamento)
      


Fimalgoritmo