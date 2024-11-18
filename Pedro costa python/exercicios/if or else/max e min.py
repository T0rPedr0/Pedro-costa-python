max = float(input("Quanto vai ser o numero maximo: "))
min = float(input("Quanto vai ser o numero minimo: "))
num = float(input("Quanto vai ser o numero numero: "))

if min < 0:
    print ("O minimo nao pode ser menor que zero") 

else:
    if num < max and num >min:
        num = "dentro"

    else:
        num = "fora"

print ("O teu numero está",num)



