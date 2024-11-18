import math
print ("Bem vindo à minha biblioteca de figuras geometricas")

r = int(input("vai procurar uma area(1) ou um volume(2): "))

match r:
    case 1:
        fig = int(input("A figura vai ser um triangulo(1), um quadrado(2), pentagono(3), um hexagono(4), um heptagono(5), um octogono(6) ou um circulo(7): "))

        match fig:
            case 1:
                print ("Qual o tipo de triangulo?")

                t = int(input("Triangulo qualquer(1) ou triangulo equilatero(2): "))

                match t:
                    case 1:
                        print ("Vamos calcular a area do triangulo")

                        lado = float(input("Quantos cm vai ser o lado: "))

                        alt = float(input("Quantos cm vai ter de altura: "))

                        area = lado * alt / 2

                        print ("A area e" ,area,"cm^2" ) 
                    
                    case 2:
                        print ("Vamos calcular a area do triangulo equilatero")

                        lado = float(input("Quantos cm vai ser o lado: "))

                        lado2 = lado / 2

                        alt = math.sqrt (lado**2 - lado2**2)

                        area = lado * alt / 2

                        print ("A area e" ,area,"cm^2" ) 

                    case _:
                        print ("tem de ser um dos numeros")
            
            case 2:
                res = int(input("vais querer um quadrado(1) ou um retangulo(2): "))

                match res:
                    case 1:
                        print ("Agora vamos calcular a area do quadrado")

                        lado = int(input("Quantos cm vai medir a lado do quadrado: "))
                        
                        area = lado * lado

                        print ("A area é" , area, "cm^2")

                    case 2:
                        print ("Agora vamos calcular a area do retangulo")

                        lado = int(input("Quantos cm vai ser o comprimento do quadrado: "))

                        lado = int(input("Quantos cm vai ter a altura do quadrado: "))
                        
                        area = lado * lado

                        print ("A area é" , area, "cm^2")

                    case _ :
                        print ("tem de ser um dos numeros")

            case 3:              
                print ("Vamos calcular a area do pentagono regular")

                lado = float(input("Quantos cm vai ser o lado: ")) 

                lado2 = lado / 2

                alt = math.sqrt (lado**2 - lado2**2)

                P = lado * 5

                A = P * alt / 2

                print ("A area e" ,A,"cm^2" ) 
            
            case 4:
                print ("Vamos calcular a area do hexagono regular")

                lado = float(input("Quantos cm vai ser o lado: ")) 

                lado2 = lado / 2

                alt = math.sqrt (lado**2 - lado2**2) 

                P = lado * 6

                A = P * alt / 2

                print ("A area e" ,A,"cm^2" ) 

            case 5:
                print ("Vamos calcular a area do heptagono regular")

                lado = float(input("Quantos cm vai ser o lado: ")) 

                lado2 = lado / 2

                alt = math.sqrt (lado**2 - lado2**2)

                P = lado * 7

                A = P * alt / 2

                print ("A area e" ,A,"cm^2" ) 

            case 6:
                print ("Vamos calcular a area do octogono regular")

                lado = float(input("Quantos cm vai ser o lado: ")) 

                ap = float(input("Quantos cm vai ser o apotma: ")) 

                P = lado * 8

                A = P * ap / 2

                print ("A area e" ,A,"cm^2" ) 

            case 7:
                print ("Vamos calcular a area do circulo")

                r = int(input("Quantos cm vai medir o raio: "))

                b = 3.14159 * r**2 

                print ("A area do circulo e de", b,"cm^2")

            case _:
                print ("tem de ser um dos numeros")

    case 2:
        V = int(input("A figura vai ser uma piramide(1), um cubo(2), um cone(3) ou esfera(4): "))

        match V:
            case 1:

                base = int(input("A base vai ser triangular(1), quadrangular(2), pentagonal(3), hexagonal(4), heptagonal(5) ou octogonal(6): "))

                match base:
                    case 1:
                        t = int(input("Triangulo qualquer(1) ou triangulo equilatero(2): "))

                        match t:
                            case 1:
                                print ("Vamos calcular o volume do triangulo com base triangular")

                                lado = float(input("Quantos cm vai ser o lado: "))

                                altb = float(input("Quantos cm vai ser o lado: "))

                                alt = float(input("Quantos cm vai ter de altura: "))

                                areab = lado * altb / 2

                                print ("A area da base e" ,areab,"cm^2" )

                                ah = areab * alt

                                V = ah / 3

                                print ("O volume e" ,V ,"cm^3" )  

                            case 2:
                                print ("Vamos calcular o volume do triangulo com base triangular equilatera")

                                lado = float(input("Quantos cm vai ser o lado: "))

                                lado2 = lado / 2

                                alt = math.sqrt (lado**2 - lado2**2)

                                area = lado * alt / 2

                                print ("A area e" ,area,"cm^2" ) 

                            case _ :
                                print ("tem de ser um dos numeros")

                    
                    case 2:
                        t = int(input("a base vai ser quadrangular(1) ou retangular(2): "))
                        
                        match t:
                            case 1:
                                print ("Vamos calcular o volume do triangulo com base quadrangular")

                                lado = float(input("Quantos cm vai ser o lado: "))

                                alt = float(input("Quantos cm vai ter de altura: "))

                                areab = lado * lado

                                print ("A area da base e" ,areab,"cm^2" )

                                ah = areab * alt

                                V = ah / 3

                                print ("O volume e" ,V ,"cm^3" )  

                            case 2:
                                print ("Vamos calcular o volume do triangulo com base retangular")

                                c = float(input("Quantos cm vai ser o comprimento da base: "))

                                alt2 = float(input("Quantos cm vai ser o comprimento da base: "))

                                alt = float(input("Quantos cm vai ter de altura: "))

                                areab = c * alt2

                                print ("A area da base e" ,areab,"cm^2" )

                                ah = areab * alt

                                V = ah / 3

                                print ("O volume e" ,V ,"cm^3" )

                            case _:
                                print ("tem de ser um dos numeros")

                    case 3:
                        print ("Vamos calcular o volume da piramide com base de pentagono regular")

                        lado = float(input("Quantos cm vai ser o lado: ")) 

                        lado2 = lado / 2

                        alt = math.sqrt (lado**2 - lado2**2)

                        P = lado * 5

                        Ab = P * alt / 2

                        print ("A area e" ,Ab,"cm^2" )

                        alt = float(input("Quantos cm vai ser a altura: ")) 

                        ah = Ab * alt

                        V = ah / 3

                        print ("O volume e" ,V ,"cm^3" )

                    case 4:
                        print ("Vamos calcular o volume da piramide com base de hexagono regular")

                        lado = float(input("Quantos cm vai ser o lado: ")) 

                        lado2 = lado / 2

                        alt = math.sqrt (lado**2 - lado2**2)

                        P = lado * 6

                        Ab = P * alt / 2

                        print ("A area e" ,Ab,"cm^2" )

                        alt = float(input("Quantos cm vai ser a altura: ")) 

                        ah = Ab * alt

                        V = ah / 3

                        print ("O volume e" ,V ,"cm^3" )

                    case 5:
                        print ("Vamos calcular o volume da piramide com base de heptagono regular")

                        lado = float(input("Quantos cm vai ser o lado: ")) 

                        lado2 = lado / 2

                        alt = math.sqrt (lado**2 - lado2**2)

                        P = lado * 7

                        Ab = P * alt / 2

                        print ("A area e" ,Ab,"cm^2" )

                        alt = float(input("Quantos cm vai ser a altura: ")) 

                        ah = Ab * alt

                        V = ah / 3

                        print ("O volume e" ,V ,"cm^3" )

                    case 6:
                        print ("Vamos calcular o volume da piramide com base de octogono regular")

                        lado = float(input("Quantos cm vai ser o lado: ")) 

                        lado2 = lado / 2

                        alt = math.sqrt (lado**2 - lado2**2)

                        P = lado * 8

                        Ab = P * alt / 2

                        print ("A area e" ,Ab,"cm^2" )

                        alt = float(input("Quantos cm vai ser a altura: ")) 

                        ah = Ab * alt

                        V = ah / 3

                        print ("O volume e" ,V ,"cm^3" )

                    case _:
                        print ("tem de ser um dos numeros")


            case 2:
                t = int(input("cubo(1) ou retangulo(2): "))

                match t:
                    case 1 :
                        print ("Vamos calcular o volume do cubo")

                        l= float(input("Quantos cm vai ser o lado do cubo: "))

                        V = l**3

                        print ("O cubo tem",V,"cm^3")

                    case 2:
                        print ("Vamos calcular o volume do retangulo")

                        c= float(input("Quantos cm vai ser o comprimento do retangulo: "))

                        l= float(input("Quantos cm vai ser a largura do retangulo: "))

                        alt= float(input("Quantos cm vai ser a altura do retangulo: "))

                        V = c * l * alt

                        print ("O cubo tem",V,"cm^3")

                    case _ :
                        print ("tem de ser um dos numeros")
                        


            case 3:
                print ("Vamos calcular o volume do cone")

                r = float(input("Quantos cm vai medir o raio: "))

                Ab = r**2 * 3.14159

                alt = float(input("Quantos cm vai ter de altura: "))

                R = Ab * alt / 2

                print ("O volume do cone e de:",R,"cm^3")

            case 4:
                print ("Vamos calcular o volume da esfera")

                r = float(input("Quantos cm vai sai ser o raio: "))

                V = 3.14159 * r**3 / 1.333333

                print ("O volume da esfera e de:", V,"cm^3")

            case _ :
                print ("tem de ser um dos numeros")