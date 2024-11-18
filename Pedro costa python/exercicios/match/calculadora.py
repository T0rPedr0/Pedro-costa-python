print ("Vamos fazer uma conta")

num1 = float(input("qual vai ser o primeiro numero: "))

num2 = float(input("qual vai ser o segundo numero: "))

sinal = input("qual o sinal da operaçao,(+ ; - ; * ; :) ")

match sinal:
    case "+" :
         num = num1 + num2
         print ("O resultado da soma é", num)

    case "-" :
         num = num1 - num2
         print ("O resultado da subtraçao é", num)

    case "*" :
         num = num1 * num2
         print ("O resultado da multiplicaçao é", num)

    case ":" :
         num = num1 / num2
         print ("O resultado da divisao é", num)
