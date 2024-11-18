print ("Agora vamos calcular a rapidez media")

u = int(input("O intervalo de tempo foi em segundos(1) ou em horas(2): "))

match u:
    case 1:
        medida = str(input("A distancia foi percorrida em metros(m) ou em kilometros(km): "))

        match medida:

            case 1:

                s1 = float(input("Quantos kilometros foram percorridos: "))

                s = s1 / 1000

            case 2:
                s = float(input("Quantos metros foram percorridos: "))

            case 3:
                s1 = float(input("Quantos kilometros foram percorridos: "))

                s = s1 * 1000

            case _:
                print("Tens de escolher um dos numeros")

        T = float(input("Qual foi o tempo do intervalo de tempo: "))

        rm = s / T

        rm1 = rm / 1000

        rm2 = rm1 * 3600



    case 2:

        h1 = int(input("Qual a hora inicial: "))

        m1 = int(input("Qual os minutos iniciais: "))

        h2 = int(input("Qual a hora final: "))

        m2 = int(input("Qual os minutos final: "))

        if h1 > 24 or h2 > 24:
            print ("A hora nao pode ser maior que 24 horas")

        elif m1 > 60 or m2 > 60:
            print ("Os minutos nao pode ser maior que 60 minutos")

        else:
            t1 = h2 - h1   

            t2 = m2 - m1   

            t3 = t1 * 60 + t2   

            if t1 < 0 or t3 < 0:
                print ("O tempo inicial nao pode ser maior que o tempo final")

            else:
                print ("O intervalo de tempo é",t1,"H",t2,"min")

                medida = str(input("A distancia foi percorrida em metros(m) ou em kilometros(km): "))

                if medida == "km":
                    s1 = float(input("Quantos kilometros foram percorridos: "))

                    s = s1 * 1000

                else:
                    s = float(input("Quantos metros foram percorridos: "))

                T = t3 / 60

                rm = s / T

                rm1 = rm / 1000

                rm2 = rm1 * 3600

    case _ :

        print("Tens de escolher um dos numeros")

print ("A rapidez media é",rm,"m/s ou",rm2,"km/h")