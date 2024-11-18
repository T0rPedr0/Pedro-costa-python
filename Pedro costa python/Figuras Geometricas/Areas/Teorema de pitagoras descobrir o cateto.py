import math

print ("Vamos calcular o teorema de pitagoras")

h = float(input("quanto vai ser a hipotenusa: "))

c2 = float(input("quanto vai ser o segundo cateto: "))

c1 = math.sqrt (h**2 - c2**2)

print ("O tamanho da hipotenusa e", c1)