print ("Vamos ver quando é  que nasceste")

res = str(input("Já fizeste anos: "))

if res == "sim":
    idade = int(input("Qual a tua idade: "))
    ano = 2024 - idade 
    print ("tu tens",ano,"anos")

else:
    idade = int(input("Qual a tua idade: "))
    ano = 2024 - idade -1
    print ("tu tens",ano,"anos")