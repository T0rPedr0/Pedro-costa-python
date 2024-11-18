import random
import time

i = "What a sigma 🗿🍷"

armadura = 0

dinheiro = 0

cigarros = 0

print("Historia")

print("O reino de Eldória está à beira do caos. O rei foi assassinado, e o trono está vazio.")

print("Tu mero habitante suspeitas de que há uma assassino entre os habitantes do reino.")

time.sleep(5)

def Praça (armadura,dinheiro,cigarros):

    while i:

        ação_sair_Praça = int(input("Permanecer na praça(1); sair para o beco escuro(2) ou sair para porta do castelo(3): "))

        match ação_sair_Praça:
            case 1:
                print("Tu estás na praça principal do reino")

                print("Na praça está muita gente, com quem queres falar?")

                ação_Praça = int(input("Uma criança com balão(1); o Ferreiro(2); um Comerciante(3) ou uma homem a fumar à beira da fonte(4): "))

                match ação_Praça:
                    case 1:
                        print("Tu vais falar com a criança do balão")

                        time.sleep(4)

                        print("Ela é muito pequena e quando tentas falar com ela sobre o assassinato do rei ela não entende")

                    case 2:
                        
                        print("Tu vais falar com o Ferreiro")

                        time.sleep(4)

                        if armadura == 0:

                            print("Ele diz que no dia do crime estava ocupado a comprar mais metais com o comerciante, mas que se estiveces entereçado ele podia vender uma armadura")

                            comprar_armadura = int(input("Sim(1) ou Não(2): "))

                            if comprar_armadura == 1:
                                if dinheiro == 0:
                                    print("Tu não tens dinheiro")

                                else:
                                    dinheiro += -1

                                    armadura += 1

                                    print("Tu compraste a armadura")

                        else:
                            print("Ele diz que no dia do crime estava ocupado a comprar mais metrais com o comerciante")
                            
                    case 3:
                        print("Tu decides falar com o comerciante")

                        print("Ele diz estar a vender coisas para o ferreiro nessa noite")

                    case 4:
                        print("Tu decides falar com o homem a fumar a beira da fonte")

                        if cigarros == 0:
                            print("Homem: Vai-te embora")

                            print("Parece que os cigarros dele estão a acabar")

                        else:
                            print("Podes me dar um cigarro")

                            cigarros_ação = int(input("Dar cigarros(1) ou não dar(2): "))

                            if cigarros_ação == 1:
                                print("Homem: Só vou dizer uma vez, eu vi o ferreiro e o comerciante juntos no beco escuro e eles pareciam muito suspeitos")

                                cigarros += -1

                            else:
                                print("Então vai embora")

                    case _:
                        print("Tens de escolher uma das opções")

            case 2:
                def Beco_Escuro (dinheiro):

                    print("Tu estás no beco escuro")

                    print("No beco estão umas pessoas muito estranhas")

                    while i:

                        ação_sair_Beco =int(input("Queres continuar no beco escuro(1); sair para a praça(2): "))

                        match ação_sair_Beco:
                            case 2:
                                Praça(armadura,dinheiro,cigarros)

                            case 1:
                                print ("Com quem queres falar")

                                ação_Beco = int(input("Esquisofremico(1),altista(2) ou Homem Bebado(3): "))

                                match ação_Beco:
                                    case 1:
                                        print("Tu decides falar com o esquisofremico")

                                        time.sleep(3)

                                        print("Esquisofremico: 1 9 25 18 22 5 2 1 2 14 20 5 23 5 24 1 24 14 4 7 1 4 1 9 1 20 14 24 9 4 5 26 23 14")

                                    case 2:
                                        print ("Ele quer jogar com tigo pedra papel tesoura, o que tu fazes?")

                                        ação_sair_esquisofremico = int(input("Jogar(1) ou Sair(2): "))

                                        match ação_sair_esquisofremico:
                                            case 2:
                                                print("Ele fica muito chateado mas tu sais")

                                            case 1:

                                                while i:

                                                    ação_esquisofremico =[1,2,3]

                                                    random.choice(ação_esquisofremico)

                                                    print ("Qual vai ser a tua ação?")

                                                    ação_jogo= int(input("Pedra(1); Papel(2) ou Tesoura(3): "))

                                                    match ação_esquisofremico:
                                                        case 1:
                                                            match ação_jogo:
                                                                case 1:
                                                                    print("Empate")

                                                                    print("Ambos escolherem pedra")

                                                                case 2:
                                                                    print ("Ganhaste")

                                                                    print ("O papel esmaga a pedra")

                                                                    print("Ganhaste algum dinheiro")

                                                                    dinheiro += 1

                                                                    break
                                                                
                                                                case 3:
                                                                    print("Perdeste")

                                                                    print ("A pedra esmaga a tesoura")

                                                        case 2:
                                                            match ação_jogo:
                                                                case 2:
                                                                    print("Empate")

                                                                    print("Ambos escolherem papel")

                                                                case 3:
                                                                    print ("Ganhaste")

                                                                    print ("A tesoura esmaga o papel")

                                                                    print("Ganhaste algum dinheiro")

                                                                    dinheiro += 1

                                                                    break
                                                                
                                                                case 1:
                                                                    print("Perdeste")

                                                                    print ("O papel esmaga a pedra")

                                                        case 3:
                                                            match ação_jogo:
                                                                case 3:
                                                                    print("Empate")

                                                                    print("Ambos escolherem tesoura")

                                                                case 1:
                                                                    print ("Ganhaste")

                                                                    print ("A pedra esmaga a tesoura")

                                                                    print("Ganhaste algum dinheiro")

                                                                    dinheiro += 1

                                                                    break
                                                                
                                                                case 2:
                                                                    print("Perdeste")

                                                                    print ("A tesoura esmaga o papel")

                                    case 3:
                                        print("Tu decides falar com o homem bebado")

                                        print("Ele está muito bebado mas fala algo sobre o comerciante")

                                        print("Tu não entendes o que ele diz")

                Beco_Escuro(dinheiro)

            case 3:
                def Porta_Castelo (armadura,dinheiro):

                    print ("Tu estás na porta do castel")       

                    print ("Tem varios guardas á porta")

                    while i:
                        ação_sair_Porta_Castelo = int(input("Permanecer na porta do castelo(1); entrar no castelo(2) ou Sair para a praça(3): "))
                    
                        match ação_sair_Porta_Castelo:
                            case 3:
                                Praça(armadura,dinheiro,cigarros)

                            case 1:
                                print ("Tu falas com os Guardas")

                                print ("Guardas: Sabes quem é o culpado?")

                                ação_Porta_do_castelo =  int(input("Sim(1) ou Não(2): "))

                                if ação_Porta_do_castelo == 1:

                                    print("Quem é o culpado?")

                                    culpado = int(input("Miudo do balão(1); Ferreiro(2); Comerciante(3); Homem a fumar(4); esquisofremico(5); altista(6) ou bebado(7): "))

                                    if culpado == 3:
                                        print("Parabens acertaste")

                                        print("graças a ti o culpado foi presoe todos estão felizes agora")

                                    else:
                                        print ("Infelizmente erraste e ele/a foi preso/a injustamente")

                                    exit()
                Porta_Castelo(armadura,dinheiro)
Praça(armadura,dinheiro,cigarros)