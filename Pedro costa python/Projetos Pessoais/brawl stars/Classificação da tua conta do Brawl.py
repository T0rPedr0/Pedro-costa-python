print ("Vamos testar a raridade da tua conta do Brawl Stars")

trofeus = int(input("Quantos trofeus tens: "))
if trofeus < 0:
    print ("Tens de colocar um numero positivo")

else:
    if trofeus < 1000:
        trofeus1 = 1

    elif trofeus > 1000 and trofeus < 5000:
        trofeus1 = 5

    elif trofeus > 5000 and trofeus < 10000:
        trofeus1 = 10

    elif trofeus > 10000 and trofeus < 15000:
        trofeus1 = 15

    elif trofeus > 15000 and trofeus < 20000:
        trofeus1 =  20

    elif trofeus > 20000 and trofeus < 25000:
        trofeus1 = 25

    elif trofeus > 25000 and trofeus < 30000:
        trofeus1 = 30

    else:
        trofeus1 = 40

    Brawlers = int(input("Quantos Brawlers tens: "))

    if Brawlers < 0:
        print ("Tens de colocar um numero positivo")
    
    else:
        if Brawlers < 10:
            Brawlers1 = 3

        elif Brawlers > 10 and Brawlers < 20:
            Brawlers1 = 8

        elif Brawlers > 20 and Brawlers < 30:
            Brawlers1 = 15

        elif Brawlers > 30 and Brawlers < 40:
            Brawlers1 = 20

        elif Brawlers > 40 and Brawlers < 50:
            Brawlers1 = 25

        elif Brawlers > 50 and Brawlers < 60:
            Brawlers1 = 30

        elif Brawlers > 60 and Brawlers < 70:
            Brawlers1 = 33

        elif Brawlers > 70 and Brawlers < 80:
            Brawlers1 = 36

        else:
            Brawlers1 = 40

        titulos = int(input("Quanto titulos de brawlers têm: "))

        if titulos < 0:
            print("Tens de colocar um numero positivo")

        else:
            if titulos == 0:
                titulos1 = 0

            elif titulos == 1:
                titulos1 = 10

            elif titulos == 2:
                titulos1 = 20

            elif titulos == 3:
                titulos1 = 30

            elif titulos == 4:
                titulos1 = 35

            else:
                titulos1 = 40

            ano = int(input("Quando criaste a conta: "))

            if ano < 2014:
                print("O Brawl nem existia nessa alura")
                
            elif ano == 2024:
                    ano1 = 5

            elif ano < 2024 and ano > 2020:
                    ano1 = 20

            else:
                ano1 = 40

            pontos = trofeus1 + Brawlers1 + titulos1 + ano1

            print(pontos,"pontos")

            if pontos < 50:
                print("Conta nivel F")

            elif pontos >= 50 and pontos < 80:
                print ("Conta nivel D")

            elif pontos >= 80 and pontos < 110:
                print ("Conta nivel C")

            elif pontos >= 110 and pontos < 130:                    
                print ("Conta nivel B")

            elif pontos >= 130 and pontos < 155:
                print ("Conta nivel A")

            else:
                print ("Conta nivel S")
                