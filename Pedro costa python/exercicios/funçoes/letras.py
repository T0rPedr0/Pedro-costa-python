# perguntar a frase e as letra

# ver quantas letras iguais tem a frase

# dizer quantas letra iguais tem

frase = input("Diz uma frase: ")

letra = input("Qual a letra que queres verificar: ")

def Letra ():
    n_de_letras=0
    for i in frase:

        if i == letra:

            n_de_letras +=1 
    print("Esta frase tem",n_de_letras,"letra",letra)

Letra()
