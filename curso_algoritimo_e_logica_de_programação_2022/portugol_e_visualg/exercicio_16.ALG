Algoritmo "semnome"
//Problema "senha_fixa" (adaptado de URI 1114)
//Escreva um programa que repita a leitura de uma senha até que ela seja válida. Para cada leitura de
//senha incorreta informada, escrever a mensagem "Senha Invalida! Tente novamente:". Quando a senha
//for informada corretamente deve ser impressa a mensagem "Acesso Permitido" e o algoritmo
//encerrado. Considere que a senha correta é o valor 2002. 



Var

   senha, senha_digitada : inteiro

Inicio

   senha <- 2312
   
   escreval("Digite a senha: ", senha)
   leia(senha_digitada)

   enquanto senha_digitada <> senha faca
      escreval("senha invalida ! Tente Novamente :")
      leia(senha_digitada)
   fimenquanto
   
   se senha = senha_digitada entao
      escreval("Acesso permitido!")
   fimse


Fimalgoritmo