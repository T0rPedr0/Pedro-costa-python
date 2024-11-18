print("Vamos calcular a media")

num = int(input("Qual o primeiro numero: "))

num2 = int(input("E agora o teu segundo numero: "))

soma = num + num2 

media = soma / 2

if  media < 60:

    media = "reprovado"
        
else: 
     
    media = "aprovado"

print ("a tu estas" , media)