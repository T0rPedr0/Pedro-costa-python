print ("Vamos ver se o teu numero é negativo, positivo ou neutro ")

idade = int(input("Qual o teu numero: "))

if idade < 0 :
    idade = "numero negativo"

elif idade == 0:
    idade = "numero neutro"

else:
    idade = "numero positivo"

print("O numro é um", idade)