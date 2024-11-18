v = int(input("Qual a velocidade que passaste no radar: "))

if v > 80:
    multa = (v- 80) * 2 

    print ("Tu tens de pagar",multa,"euros")

else:
    print ("tudo certo podes proseguir")