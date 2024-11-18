print ("Vamos ver a tua idade para saber se és adolescente ou nao")

idade = int(input("Qual a tua idade: "))

if idade < 18 :
    idade = "vais nanar criança"

elif idade == 18:
    idade = "agora podes trabalhar"

else:
    idade = "estas quase na reforma"

print("Tu", idade)