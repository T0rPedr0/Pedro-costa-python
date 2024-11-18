print ("Vamos calcular quantos cubos cabem dentro de um outro cubo")

l1= float(input("Quantos cm vai ser o lado do cubo 1: "))

V1 = l1**3

print ("O cubo 1 tem",V1,"cm^3 de volume")

l2 = float(input("Quantos cm vai ser o lado do cubo 2: "))

V2 = l2**3 

print ("O cubo 2 tem",V2,"cm^3 de volume")

R = V2 / V1 

print ("Cabem dentro do cubo 2:", R, "cubos 1")