num1 = int(input("Qual vai ser o primeiro numero: "))

num2 = int(input("Qual vai ser o segundo numero: "))

def soma():
    num3 = num1 + num2

    print(num3)

def subtração ():
    num3 = num1 - num2

    print(num3)

def multiplicação ():
    num3 = num1 * num2
  
    print(num3)

def divisao ():
    num3 = num1 / num2

    print(num3)

print("Qual vai ser a operacão?")
operaçao = int(input("soma(1); subtração(2); multiplicação(3) ou divisão(4) "))

match operaçao:
    case 1:
        soma()

    case 2:
        subtração()

    case 3:
        multiplicação()

    case 4:
        divisao()