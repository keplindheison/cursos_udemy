Algoritmo "semnome"
//Problema "troco"
//Fazer um programa para calcular o troco no processo de pagamento de
//um produto de uma mercearia.
//O programa deve ler o preço unitário do produto, a quantidade de unidades
//compradas deste produto,
//e o valor em dinheiro dado pelo cliente (suponha que haja dinheiro suficiente).
//Seu programa deve
//mostrar o valor do troco a ser devolvido ao cliente.
Var

   valor_produto, valor_recebido, troco, valor_total : real
   quantidade : inteiro


Inicio
      escreval("Digite o valor unitario do produto: R$ ")
      leia(valor_produto)
      escreval("Digite a quantidade comprada: ")
      leia(quantidade)

      valor_total <- quantidade * valor_produto
      escreval("Valor da compra é de R$", valor_total)
      
      escreval("Valor recebido: R$")
      leia(valor_recebido)
      
      troco <- valor_recebido - valor_total
      
      escreval("seu troco é R$", troco)
      
      


Fimalgoritmo