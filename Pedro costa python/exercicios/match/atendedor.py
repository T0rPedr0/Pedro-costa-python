num = int(input("Digite um numero entra 1 a 3: "))

match num:
    case 1:
        print ("Bem vindo")

    case 2:
        print ("8 x 6 = 48")

    case 3:
        print ("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")
    case _:
        print("O numero tem de ser entre 1 a 3")