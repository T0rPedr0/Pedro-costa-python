min = 999999999999999999999999999999999999999999999999999999999999999999999
max =-999999999999999999999999999999999999999999999999999999999999999999999
for x in range (5):

    peso = int(input("diz  quanto pesa o primeiro peso: "))

    if peso > max:
        max = peso

    if peso < min:
        min = peso

print ("O maximo é",max,"e  minimo é",min)