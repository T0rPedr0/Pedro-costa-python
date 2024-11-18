print ("Vamos calcular quantas piramides cabem dentro de um cubo")

lado = float(input("Quantos cm vai ser o lado da base da piramide: "))

alt = float(input("Quantos cm vai ter de altura da piramide: "))

areab = lado * lado

print ("A area da base e" ,areab,"cm^2" )

ah = areab * alt

V = ah / 3

print ("O volume e" ,V ,"cm^3" )  

l1= float(input("Quantos cm vai ser o lado do cubo: "))

V1 = l1**3

print ("O cubo tem",V1,"cm^3 de volume")

R = V1 / V

print ("Cabem dentro do cubo:", R, "piramides")