import random
import time

# Estatisticas

preçoAtk = 30

preçoDef = 30

preçoHp = 30

loop = 3

Hpmax = 100

HP = 100

ATK = 20

Def = 10

poções_de_cura = 3

dinheiro = 0

ponto = 0


print ("Introdução:")

print("És um herói em busca de aventura até que encontas uma guilda de aventureiros e decides procurar um trabalho")

time.sleep(4)

nome = input("Recepcionista: Qual o teu nome?: ")

print ("Recepcionista: Olá",nome,"eu tenho uma aventura perfeita para ti, matar monstros e ganhar dinheiro com isso")

time.sleep(6)

print ("Tu começas a andar pela floresta")

time.sleep(2)

print ("Status:")

print ("HP: 100")

print("Atk: 20")

print("Def: 10")

print("Dinheiro: 0")

print("E tens 3 poções de cura")

time.sleep(10)

for i in range (3):        # Primeiras rodadas de inimigos easy

    inimigos = [1,2,3]          # (1 é cobra) (2 é siclope anao) (3 é raposa)

    inimigo1 = random.choice(inimigos)
    match inimigo1:
        case 1:           

            print ("Parece que apareceu uma cobra no caminho e ela está pronta para te atacar")

            HPc = 38

            ATKc = 17 or 14

            Defc = 10

            while i:
                
                print("Qual será a tua ação?")

                time.sleep(1)

                ação = int(input("Atacar(1); Curar(2); Examinar(3): "))

                time.sleep(1)

                match ação:
                    case 1:
                        dano = [1,2]

                        dano1 = random.choice(dano)
                        
                        match dano1:
                            case 1:

                                Dano_Total_c = -Defc + ATK + 4

                                HPc += - Dano_Total_c

                                print("Tu deste",Dano_Total_c,"de dano")

                                time.sleep(3)

                            case 2:
                                Dano_Total_c = -Defc + ATK

                                HPc += - Dano_Total_c

                                print("Tu deste",Dano_Total_c,"de dano")

                                time.sleep(3)

                        if HPc < 0:

                            ponto += 17
                                
                            dinheiroc = [1,2,3]

                            dinheiroc1 = random.choice(dinheiroc)

                            match dinheiroc1:
                                case 1:
                                    print("Tu mataste a cobra e ganhaste 17 moedas")

                                    dinheiro += 17

                                case 2:
                                    print("Tu mataste a cobra e ganhaste 15 moedas")

                                    dinheiro += 15

                                case 3:
                                    print("Tu mataste a cobra e ganhaste 16 moedas")

                                    dinheiro += 16
                            
                            break

                    case 2:

                        if poções_de_cura < 0:
                            
                            print("Tu não tens poções de cura suficientes")

                            time.sleep(3)

                        else:

                            poções_de_cura += -1

                            HP += 30

                            print("Tomaste uma poção de cura e curaste 30 de vida")

                            time.sleep(3)

                    case 3: 

                        print("A cobra tem",HPc,"de Hp",ATKc,"de Atk e",Defc,"de Def")

                        print("Esta cobra tem uma pele bastante resistente")

                        time.sleep(10)
                    
                print("A cobra vai atacar")

                Ataques = [1,2]

                Ataque1 = random.choice(Ataques)

                match Ataque1:
                    case 1:

                        HP += -17 

                        print("A cobra usou o ataque rabo de chicote e deu 17 de dano")

                    case 2:

                        HP += -14

                        print("A cobra usou o ataque presas afiadas e deu 14 de dano")

                if HP < 0:

                    print("Tu morreste")

                    print("Tu tiveste",ponto,"ponto")
                    
                    exit()

                print("Tu tens",HP,"de Hp e",poções_de_cura,"poções de cura")

        case 2:
            print ("Parece que apareceu um siclop anão no caminho e ele está pronto para te atacar")

            HPs = 60

            ATKs = 18 or 21

            Defs = 3

            while i:
                
                print("Qual será a tua ação?")

                time.sleep(1)

                ação = int(input("Atacar(1); Curar(2); Examinar(3): "))

                time.sleep(1)

                match ação:
                    case 1:
                        dano = [1,2]

                        dano1 = random.choice(dano)
                        
                        match dano1:
                            case 1:

                                Dano_Total_s = -Defs + ATK + 4

                                HPs += - Dano_Total_s

                                print("Tu deste",Dano_Total_s,"de dano")

                                time.sleep(3)

                            case 2:
                                Dano_Total_s = -Defs + ATK

                                HPs += - Dano_Total_s

                                print("Tu deste",Dano_Total_s,"de dano")

                                time.sleep(3)

                        if HPs < 0:

                            ponto += 25
                                
                            dinheiros = [1,2,3]

                            dinheiros1 = random.choice(dinheiros)

                            match dinheiros1:
                                case 1:
                                    print("Tu mataste o siclope anão e ganhaste 24 moedas")

                                    dinheiro += 24

                                case 2:
                                    print("Tu mataste o siclope anão e ganhaste 23 moedas")

                                    dinheiro += 23

                                case 3:
                                    print("Tu mataste o siclope anão e ganhaste 25 moedas")

                                    dinheiro += 25
                            
                            break

                    case 2:

                        if poções_de_cura < 0:
                            
                            print("Tu não tens poções de cura suficientes")

                            time.sleep(3)

                        else:

                            poções_de_cura += -1

                            HP += 30

                            print("Tomaste uma poção de cura e curaste 30 de vida")

                            time.sleep(3)

                    case 3: 

                        print("O siclope anão tem",HPs,"de Hp",ATKs,"de Atk e",Defs,"de Def")

                        print("Este siclope está seminu")

                        time.sleep(10)
                    
                print("O siclope anão vai atacar")

                Ataques = [1,2]

                Ataque1 = random.choice(Ataques)

                match Ataque1:
                    case 1:

                        HP += -18

                        print("O siclope anão usou o ataque barte com borrete e deu 18 de dano")

                    case 2:

                        HP += -21

                        print("O siclope anão usou o ataque olhar sigma 🗿🍷 e deu 21 de dano")

                if HP < 0:

                    print("Tu morreste")

                    print("Tu tiveste",ponto,"ponto")
                    
                    exit()

                print("Tu tens",HP,"de Hp e",poções_de_cura,"poções de cura")

        case 3:
            print ("Parece que apareceu uma raposa no caminho e ele está pronto para te atacar")

            HPr = 45

            ATKr = 22 or 24

            Defr = 4

            while i:
                
                print("Qual será a tua ação?")

                time.sleep(1)

                ação = int(input("Atacar(1); Curar(2); Examinar(3): "))

                time.sleep(1)

                match ação:
                    case 1:
                        dano = [1,2]

                        dano1 = random.choice(dano)
                        
                        match dano1:
                            case 1:

                                Dano_Total_r = -Defr + ATK + 4

                                HPr += - Dano_Total_r

                                print("Tu deste",Dano_Total_r,"de dano")

                                time.sleep(3)

                            case 2:
                                Dano_Total_r = -Defr + ATK

                                HPr += - Dano_Total_r

                                print("Tu deste",Dano_Total_r,"de dano")

                                time.sleep(3)

                        if HPr < 0:

                            ponto += 30
                                
                            dinheiror = [1,2,3]

                            dinheiror1 = random.choice(dinheiror)

                            match dinheiros1:
                                case 1:
                                    print("Tu mataste a raposa e ganhaste 24 moedas")

                                    dinheiro += 26

                                case 2:
                                    print("Tu mataste a raposa e ganhaste 23 moedas")

                                    dinheiro += 25

                                case 3:
                                    print("Tu mataste a raposa e ganhaste 25 moedas")

                                    dinheiro += 27
                            
                            break

                    case 2:

                        if poções_de_cura < 0:
                            
                            print("Tu não tens poções de cura suficientes")

                            time.sleep(3)

                        else:

                            poções_de_cura += -1

                            HP += 30

                            print("Tomaste uma poção de cura e curaste 30 de vida")

                            time.sleep(3)

                    case 3: 

                        print("A raposa tem",HPr,"de Hp",ATKr,"de Atk e",Defr,"de Def")

                        print("A raposa tem dentes e unhas muito afiados")

                        time.sleep(10)
                    
                print("A raposa vai atacar")

                Ataques = [1,2]

                Ataque1 = random.choice(Ataques)

                match Ataque1:
                    case 1:

                        HP += -24

                        print("A Raposa usou o ataque mordida feroz e deu 24 de dano")

                    case 2:

                        HP += -21

                        print("A raposa usou o ataque unhas afiadas e deu 21 de dano")

                if HP < 0:

                    print("Tu morreste")

                    print("Tu tiveste",ponto,"ponto")
                    
                    exit()

                print("Tu tens",HP,"de Hp e",poções_de_cura,"poções de cura")

time.sleep(3)

print("Depois de",nome,"ter enfrentado diversos inimigos ele/a encontrou uma loja")

print(nome,"decidiu entrar na loja")

time.sleep(5)

print("Vendedor:Olá caro viajante o que desejas na minha humilde loja")

while i:              # Loja 1
    if i:

        time.sleep(3)

        print("Qual vai ser a tua ação")

        açãov = int(input("Comprar(1) ou sair(2): "))

        if açãov == 1:

            print("Itens á venda:")

            print("Poções de Cura-15 moedas(1); [+5 ATK]-",preçoAtk,"moedas(2); [+5 Def]-",preçoDef,"moedas(3); [+10 Hp]-",preçoDef,"moedas(4) ou sair(5): ")

            açãov1 = int(input("O que vais comprar: "))

            if açãov1 == 1:

                if dinheiro <15:
                    print("Não tens dinheiro suficiente")

                else:
                    poções_de_cura += 1

                    dinheiro += -15

                    print("Tu compraste uma poção de cura")

            elif açãov1 == 2:

                if dinheiro < preçoAtk:
                    print("Não tens dinheiro suficiente")

                else:
                    ATK += 5

                    preçoAtk += 5

            elif açãov1 == 3:

                if dinheiro < preçoDef:
                    print("Não tens dinheiro suficiente")

                else:
                    Def += 5

                    preçoDef += 5

            elif açãov1 == 4:

                if dinheiro < preçoHp:
                    print("Não tens dinheiro suficiente")

                else:
                    HP += 10

                    Hpmax += 10

                    preçoHp += 5

            else:
                
                if HP < Hpmax:
                    Hp = Hpmax
                break

        else:
            if HP < Hpmax:
                Hp = Hpmax
            break

print("Tu descides dair da loja")


for i in range (1):        # Segunda rodadas de inimigos normal

    inimigos = [1,2,3,4]          # (1 é cobra) (2 é siclope anao) (3 é raposa) (4 é inimigos V2)

    inimigosV2 = [1,2,3]

    inimigo1 = random.choice(inimigos)
    match inimigo1:
        case 1:           

            print ("Parece que apareceu uma cobra no caminho e ela está pronta para te atacar")

            HPc = 38

            ATKc = 17 or 14

            Defc = 10

            while i:
                
                print("Qual será a tua ação?")

                time.sleep(1)

                ação = int(input("Atacar(1); Curar(2); Examinar(3): "))

                time.sleep(1)

                match ação:
                    case 1:
                        dano = [1,2]

                        dano1 = random.choice(dano)
                        
                        match dano1:
                            case 1:

                                Dano_Total_c = -Defc + ATK + 4

                                HPc += - Dano_Total_c

                                print("Tu deste",Dano_Total_c,"de dano")

                                time.sleep(3)

                            case 2:
                                Dano_Total_c = -Defc + ATK

                                HPc += - Dano_Total_c

                                print("Tu deste",Dano_Total_c,"de dano")

                                time.sleep(3)

                        if HPc < 0:

                            ponto += 17
                                
                            dinheiroc = [1,2,3]

                            dinheiroc1 = random.choice(dinheiroc)

                            match dinheiroc1:
                                case 1:
                                    print("Tu mataste a cobra e ganhaste 17 moedas")

                                    dinheiro += 17

                                case 2:
                                    print("Tu mataste a cobra e ganhaste 15 moedas")

                                    dinheiro += 15

                                case 3:
                                    print("Tu mataste a cobra e ganhaste 16 moedas")

                                    dinheiro += 16
                            
                            break

                    case 2:

                        if poções_de_cura < 0:
                            
                            print("Tu não tens poções de cura suficientes")

                            time.sleep(3)

                        else:

                            poções_de_cura += -1

                            HP += 30

                            print("Tomaste uma poção de cura e curaste 30 de vida")

                            time.sleep(3)

                    case 3: 

                        print("A cobra tem",HPc,"de Hp",ATKc,"de Atk e",Defc,"de Def")

                        print("Esta cobra tem uma pele bastante resistente")

                        time.sleep(10)
                    
                print("A cobra vai atacar")

                Ataques = [1,2]

                Ataque1 = random.choice(Ataques)

                match Ataque1:
                    case 1:

                        HP += -17 

                        print("A cobra usou o ataque rabo de chicote e deu 17 de dano")

                    case 2:

                        HP += -14

                        print("A cobra usou o ataque presas afiadas e deu 14 de dano")

                if HP < 0:

                    print("Tu morreste")

                    print("Tu tiveste",ponto,"ponto")
                    
                    exit()

                print("Tu tens",HP,"de Hp e",poções_de_cura,"poções de cura")

        case 2:
            print ("Parece que apareceu um siclop anão no caminho e ele está pronto para te atacar")

            HPs = 60

            ATKs = 18 or 21

            Defs = 3

            while i:
                
                print("Qual será a tua ação?")

                time.sleep(1)

                ação = int(input("Atacar(1); Curar(2); Examinar(3): "))

                time.sleep(1)

                match ação:
                    case 1:
                        dano = [1,2]

                        dano1 = random.choice(dano)
                        
                        match dano1:
                            case 1:

                                Dano_Total_s = -Defs + ATK + 4

                                HPs += - Dano_Total_s

                                print("Tu deste",Dano_Total_s,"de dano")

                                time.sleep(3)

                            case 2:
                                Dano_Total_s = -Defs + ATK

                                HPs += - Dano_Total_s

                                print("Tu deste",Dano_Total_s,"de dano")

                                time.sleep(3)

                        if HPs < 0:

                            ponto += 25
                                
                            dinheiros = [1,2,3]

                            dinheiros1 = random.choice(dinheiros)

                            match dinheiros1:
                                case 1:
                                    print("Tu mataste o siclope anão e ganhaste 24 moedas")

                                    dinheiro += 24

                                case 2:
                                    print("Tu mataste o siclope anão e ganhaste 23 moedas")

                                    dinheiro += 23

                                case 3:
                                    print("Tu mataste o siclope anão e ganhaste 25 moedas")

                                    dinheiro += 25
                            
                            break

                    case 2:

                        if poções_de_cura < 0:
                            
                            print("Tu não tens poções de cura suficientes")

                            time.sleep(3)

                        else:

                            poções_de_cura += -1

                            HP += 30

                            print("Tomaste uma poção de cura e curaste 30 de vida")

                            time.sleep(3)

                    case 3: 

                        print("O siclope anão tem",HPs,"de Hp",ATKs,"de Atk e",Defs,"de Def")

                        print("Este siclope está seminu")

                        time.sleep(10)
                    
                print("O siclope anão vai atacar")

                Ataques = [1,2]

                Ataque1 = random.choice(Ataques)

                match Ataque1:
                    case 1:

                        HP += -18

                        print("O siclope anão usou o ataque barte com borrete e deu 18 de dano")

                    case 2:

                        HP += -21

                        print("A cobra usou o ataque olhar sigma 🗿🍷 e deu 21 de dano")

                if HP < 0:

                    print("Tu morreste")

                    print("Tu tiveste",ponto,"ponto")
                    
                    exit()

                print("Tu tens",HP,"de Hp e",poções_de_cura,"poções de cura")

        case 3:
            print ("Parece que apareceu uma raposa no caminho e ele está pronto para te atacar")

            HPr = 45

            ATKr = 22 or 24

            Defr = 4

            while i:
                
                print("Qual será a tua ação?")

                time.sleep(1)

                ação = int(input("Atacar(1); Curar(2); Examinar(3): "))

                time.sleep(1)

                match ação:
                    case 1:
                        dano = [1,2]

                        dano1 = random.choice(dano)
                        
                        match dano1:
                            case 1:

                                Dano_Total_r = -Defr + ATK + 4

                                HPr += - Dano_Total_r

                                print("Tu deste",Dano_Total_r,"de dano")

                                time.sleep(3)

                            case 2:
                                Dano_Total_r = -Defr + ATK

                                HPr += - Dano_Total_r

                                print("Tu deste",Dano_Total_r,"de dano")

                                time.sleep(3)

                        if HPr < 0:

                            ponto += 30
                                
                            dinheiror = [1,2,3]

                            dinheiror1 = random.choice(dinheiror)

                            match dinheiros1:
                                case 1:
                                    print("Tu mataste a raposa e ganhaste 24 moedas")

                                    dinheiro += 26

                                case 2:
                                    print("Tu mataste a raposa e ganhaste 23 moedas")

                                    dinheiro += 25

                                case 3:
                                    print("Tu mataste a raposa e ganhaste 25 moedas")

                                    dinheiro += 27
                            
                            break

                    case 2:

                        if poções_de_cura < 0:
                            
                            print("Tu não tens poções de cura suficientes")

                            time.sleep(3)

                        else:

                            poções_de_cura += -1

                            HP += 30

                            print("Tomaste uma poção de cura e curaste 30 de vida")

                            time.sleep(3)

                    case 3: 

                        print("A raposa tem",HPr,"de Hp",ATKr,"de Atk e",Defr,"de Def")

                        print("A raposa tem dentes e unhas muito afiados")

                        time.sleep(10)
                    
                print("A raposa vai atacar")

                Ataques = [1,2]

                Ataque1 = random.choice(Ataques)

                match Ataque1:
                    case 1:

                        HP += -24

                        print("A Raposa usou o ataque mordida feroz e deu 24 de dano")

                    case 2:

                        HP += -21

                        print("A raposa usou o ataque unhas afiadas e deu 21 de dano")

                if HP < 0:

                    print("Tu morreste")

                    print("Tu tiveste",ponto,"ponto")
                    
                    exit()

                print("Tu tens",HP,"de Hp e",poções_de_cura,"poções de cura")

        case 4:

            inimigosV21 = random.choice(inimigosV2)
            match inimigosV2:
                case 1:
                    print ("Parece que apareceu uma cobra venenosa no caminho e ela está pronta para te atacar")

                    HPcv2 = 58

                    ATKcv2 = 25 or 20

                    Defcv2 = 9

                    while i:
                        
                        print("Qual será a tua ação?")

                        time.sleep(1)

                        ação = int(input("Atacar(1); Curar(2); Examinar(3): "))

                        time.sleep(1)

                        match ação:
                            case 1:
                                dano = [1,2]

                                dano1 = random.choice(dano)
                                
                                match dano1:
                                    case 1:

                                        Dano_Total_cv2 = -Defcv2 + ATK + 4

                                        HPcv2 += - Dano_Total_cv2

                                        print("Tu deste",Dano_Total_cv2,"de dano")

                                        time.sleep(3)

                                    case 2:
                                        Dano_Total_cv2 = -Defcv2 + ATK

                                        HPcv2 += - Dano_Total_cv2

                                        print("Tu deste",Dano_Total_cv2,"de dano")

                                        time.sleep(3)

                                if HPc < 0:

                                    ponto += 35
                                        
                                    dinheirocv2 = [1,2,3]

                                    dinheirocv21 = random.choice(dinheirocv2)

                                    match dinheirocv21:
                                        case 1:
                                            print("Tu mataste a cobra e ganhaste 27 moedas")

                                            dinheiro += 27

                                        case 2:
                                            print("Tu mataste a cobra e ganhaste 25 moedas")

                                            dinheiro += 25

                                        case 3:
                                            print("Tu mataste a cobra e ganhaste 26 moedas")

                                            dinheiro += 26
                                    
                                    break

                            case 2:

                                if poções_de_cura < 0:
                                    
                                    print("Tu não tens poções de cura suficientes")

                                    time.sleep(3)

                                else:

                                    poções_de_cura += -1

                                    HP += 30

                                    print("Tomaste uma poção de cura e curaste 30 de vida")

                                    time.sleep(3)

                            case 3: 

                                print("A cobra venenosa tem",HPcv2,"de Hp",ATKcv2,"de Atk e",Defcv2,"de Def")

                                print("Esta cobra tem uma pele bastante resistente")

                                time.sleep(10)
                            
                        print("A cobra venenosa vai atacar")

                        Ataques = [1,2]

                        Ataque1 = random.choice(Ataques)

                        match Ataque1:
                            case 1:

                                HP += -25 + Def

                                print("A cobra usou o ataque rabo de chicote e deu 25 de dano")

                            case 2:

                                HP += -20 + Def

                                print("A cobra usou o ataque presas afiadas venenosas e deu 20 de dano")

                        if HP < 0:

                            print("Tu morreste")

                            print("Tu tiveste",ponto,"ponto")
                            
                            exit()

                        print("Tu tens",HP,"de Hp e",poções_de_cura,"poções de cura")

                case 2:
                    print ("Parece que apareceu um Siclop Anão com Gigantismo no caminho e ele está pronto para te atacar")

                    HPsv2 = 70

                    ATKsv2 = 26 or 21

                    Defsv2 = 4

                    while i:
                        
                        print("Qual será a tua ação?")

                        time.sleep(1)

                        ação = int(input("Atacar(1); Curar(2); Examinar(3): "))

                        time.sleep(1)

                        match ação:
                            case 1:
                                dano = [1,2]

                                dano1 = random.choice(dano)
                                
                                match dano1:
                                    case 1:

                                        Dano_Total_sv2 = -Defsv2 + ATK + 4

                                        HPsv2 += - Dano_Total_s

                                        print("Tu deste",Dano_Total_sv2,"de dano")

                                        time.sleep(3)

                                    case 2:
                                        Dano_Total_sv2 = -Defsv2 + ATK

                                        HPsv2 += - Dano_Total_sv2

                                        print("Tu deste",Dano_Total_sv2,"de dano")

                                        time.sleep(3)

                                if HPsv2 < 0:

                                    ponto += 40
                                        
                                    dinheiros = [1,2,3]

                                    dinheiros1 = random.choice(dinheiros)

                                    match dinheiros1:
                                        case 1:
                                            print("Tu mataste o Siclop Anão com Gigantismo e ganhaste 34 moedas")

                                            dinheiro += 34

                                        case 2:
                                            print("Tu mataste o Siclop Anão com Gigantismo e ganhaste 33 moedas")

                                            dinheiro += 33

                                        case 3:
                                            print("Tu mataste o Siclop Anão com Gigantismo e ganhaste 35 moedas")

                                            dinheiro += 35
                                    
                                    break

                            case 2:

                                if poções_de_cura < 0:
                                    
                                    print("Tu não tens poções de cura suficientes")

                                    time.sleep(3)

                                else:

                                    poções_de_cura += -1

                                    HP += 30

                                    print("Tomaste uma poção de cura e curaste 30 de vida")

                                    time.sleep(3)

                            case 3: 

                                print("O Siclop Anão com Gigantismo tem",HPsv2,"de Hp",ATKsv2,"de Atk e",Defsv2,"de Def")

                                print("Este Siclop Anão com Gigantismo está seminu")

                                time.sleep(10)
                            
                        print("O Siclop Anão com Gigantismo vai atacar")

                        Ataques = [1,2]

                        Ataque1 = random.choice(Ataques)

                        match Ataque1:
                            case 1:

                                HP += -26

                                print("O Siclop Anão com Gigantismo usou o ataque barte com borrete e deu 26 de dano")

                            case 2:

                                HP += -21

                                print("O Siclop Anão com Gigantismo usou o ataque olhar sigma 🗿🍷 e deu 21 de dano")

                        if HP < 0:

                            print("Tu morreste")

                            print("Tu tiveste",ponto,"ponto")
                            
                            exit()

                        print("Tu tens",HP,"de Hp e",poções_de_cura,"poções de cura")

                case 3:
                    print ("Parece que apareceu um Lobo Albino no caminho e ele está pronto para te atacar")

                    HPrv2 = 55

                    ATKrv2 = 28 or 24

                    Defrv2 = 5

                    while HP == HP:
                        
                        print("Qual será a tua ação?")

                        time.sleep(1)

                        ação = int(input("Atacar(1); Curar(2); Examinar(3): "))

                        time.sleep(1)

                        match ação:
                            case 1:
                                dano = [1,2]

                                dano1 = random.choice(dano)
                                
                                match dano1:
                                    case 1:

                                        Dano_Total_rv2 = -Defrv2 + ATK + 4

                                        HPrv2 += - Dano_Total_rv2

                                        print("Tu deste",Dano_Total_rv2,"de dano")

                                        time.sleep(3)

                                    case 2:
                                        Dano_Total_rv2 = -Defrv2 + ATK

                                        HPrv2 += - Dano_Total_rv2

                                        print("Tu deste",Dano_Total_rv2,"de dano")

                                        time.sleep(3)

                                if HPrv2 < 0:

                                    ponto += 30
                                        
                                    dinheirorv2 = [1,2,3]

                                    dinheirorv21 = random.choice(dinheiror)

                                    match dinheirorv21:
                                        case 1:
                                            print("Tu mataste o Lobo Albino e ganhaste 39 moedas")

                                            dinheiro += 39

                                        case 2:
                                            print("Tu mataste o Lobo Albino e ganhaste 40 moedas")

                                            dinheiro += 40

                                        case 3:
                                            print("Tu mataste o Lobo Albino e ganhaste 41 moedas")

                                            dinheiro += 41
                                    
                                    break

                            case 2:

                                if poções_de_cura < 0:
                                    
                                    print("Tu não tens poções de cura suficientes")

                                    time.sleep(3)

                                else:

                                    poções_de_cura += -1

                                    HP += 30

                                    print("Tomaste uma poção de cura e curaste 30 de vida")

                                    time.sleep(3)

                            case 3: 

                                print("O Lobo Albino tem",HPrv2,"de Hp",ATKrv2,"de Atk e",Defrv2,"de Def")

                                print("O Lobo Albino tem dentes e unhas muito afiados")

                                time.sleep(10)
                            
                        print("O Lobo Albino vai atacar")

                        Ataques = [1,2]

                        Ataque1 = random.choice(Ataques)

                        match Ataque1:
                            case 1:

                                HP += -24 + Def

                                print("O Lobo Albino usou o ataque mordida feroz e deu 24 de dano")

                            case 2:

                                HP += -28 + Def

                                print("O Lobo Albino usou o ataque unhas afiadas e deu 21 de dano")

                        if HP < 0:

                            print("Tu morreste")

                            print("Tu tiveste",ponto,"ponto")
                            
                            exit()

                        print("Tu tens",HP,"de Hp e",poções_de_cura,"poções de cura")

while i:        # loop final do jogo hard

    loop +=1

    print("Depois de",nome,"ter enfrentado diversos inimigos ele/a encontrou uma loja")

    print(nome,"decidiu entrar na loja")

    time.sleep(5)

    print("Vendedor:Olá caro viajante o que desejas na minha humilde loja")

    while i:              # Loja 2

        time.sleep(3)

        print("Qual vai ser a tua ação")

        açãov = int(input("Comprar(1) ou sair(2): "))

        if açãov == 1:

            print("Itens á venda:")

            print("Poções de Cura-15 moedas(1); [+5 ATK]-",preçoAtk,"moedas(2); [+5 Def]-",preçoDef,"moedas(3); [+10 Hp]-",preçoDef,"moedas(4) ou sair(5): ")

            açãov1 = int(input("O que vais comprar: "))

            if açãov1 == 1:

                if dinheiro <15:
                    print("Não tens dinheiro suficiente")

                else:
                    poções_de_cura += 1

                    dinheiro += -15

                    print("Tu compraste uma poção de cura")

            elif açãov1 == 2:

                if dinheiro < preçoAtk:
                    print("Não tens dinheiro suficiente")

                else:
                    ATK += 5

                    preçoAtk += 5

            elif açãov1 == 3:

                if dinheiro < preçoDef:
                    print("Não tens dinheiro suficiente")

                else:
                    Def += 5

                    preçoDef += 5

            elif açãov1 == 4:

                if dinheiro < preçoHp:
                    print("Não tens dinheiro suficiente")

                else:
                    HP += 10

                    Hpmax += 10

                    preçoHp += 5

            else:
                
                if HP < Hpmax:
                    Hp = Hpmax
                break

        else:
            if HP < Hpmax:
                Hp = Hpmax
            break

    print("Tu descides dair da loja")

    for i in range (loop):            # Terceiras rodadas de inimigos hard
        inimigosV2 = [1,2,3,4]

        inimigosV21 = random.choice(inimigosV2)
        match inimigosV2:        # (1 é cobra venenosa) (2 é siclope anao com gigantismo) (3 é lobo alino) (4 é baú/mimico)
   
            case 1:
                        print ("Parece que apareceu uma cobra venenosa no caminho e ela está pronta para te atacar")

                        HPcv2 = 58

                        ATKcv2 = 25 or 20

                        Defcv2 = 9

                        while i:
                            
                            print("Qual será a tua ação?")

                            time.sleep(1)

                            ação = int(input("Atacar(1); Curar(2); Examinar(3): "))

                            time.sleep(1)

                            match ação:
                                case 1:
                                    dano = [1,2]

                                    dano1 = random.choice(dano)
                                    
                                    match dano1:
                                        case 1:

                                            Dano_Total_cv2 = -Defcv2 + ATK + 4

                                            HPcv2 += - Dano_Total_cv2

                                            print("Tu deste",Dano_Total_cv2,"de dano")

                                            time.sleep(3)

                                        case 2:
                                            Dano_Total_cv2 = -Defcv2 + ATK

                                            HPcv2 += - Dano_Total_cv2

                                            print("Tu deste",Dano_Total_cv2,"de dano")

                                            time.sleep(3)

                                    if HPc < 0:

                                        ponto += 35
                                            
                                        dinheirocv2 = [1,2,3]

                                        dinheirocv21 = random.choice(dinheirocv2)

                                        match dinheirocv21:
                                            case 1:
                                                print("Tu mataste a cobra e ganhaste 27 moedas")

                                                dinheiro += 27

                                            case 2:
                                                print("Tu mataste a cobra e ganhaste 25 moedas")

                                                dinheiro += 25

                                            case 3:
                                                print("Tu mataste a cobra e ganhaste 26 moedas")

                                                dinheiro += 26
                                        
                                        break

                                case 2:

                                    if poções_de_cura < 0:
                                        
                                        print("Tu não tens poções de cura suficientes")

                                        time.sleep(3)

                                    else:

                                        poções_de_cura += -1

                                        HP += 30

                                        print("Tomaste uma poção de cura e curaste 30 de vida")

                                        time.sleep(3)

                                case 3: 

                                    print("A cobra venenosa tem",HPcv2,"de Hp",ATKcv2,"de Atk e",Defcv2,"de Def")

                                    print("Esta cobra tem uma pele bastante resistente")

                                    time.sleep(10)
                                
                            print("A cobra venenosa vai atacar")

                            Ataques = [1,2]

                            Ataque1 = random.choice(Ataques)

                            match Ataque1:
                                case 1:

                                    HP += -25 + Def

                                    print("A cobra usou o ataque rabo de chicote e deu 25 de dano")

                                case 2:

                                    HP += -20 + Def

                                    print("A cobra usou o ataque presas afiadas venenosas e deu 20 de dano")

                            if HP < 0:

                                print("Tu morreste")

                                print("Tu tiveste",ponto,"ponto")
                                
                                exit()

                            print("Tu tens",HP,"de Hp e",poções_de_cura,"poções de cura")

            case 2:
                        print ("Parece que apareceu um Siclop Anão com Gigantismo no caminho e ele está pronto para te atacar")

                        HPsv2 = 70

                        ATKsv2 = 26 or 21

                        Defsv2 = 4

                        while i:
                            
                            print("Qual será a tua ação?")

                            time.sleep(1)

                            ação = int(input("Atacar(1); Curar(2); Examinar(3): "))

                            time.sleep(1)

                            match ação:
                                case 1:
                                    dano = [1,2]

                                    dano1 = random.choice(dano)
                                    
                                    match dano1:
                                        case 1:

                                            Dano_Total_sv2 = -Defsv2 + ATK + 4

                                            HPsv2 += - Dano_Total_s

                                            print("Tu deste",Dano_Total_sv2,"de dano")

                                            time.sleep(3)

                                        case 2:
                                            Dano_Total_sv2 = -Defsv2 + ATK

                                            HPsv2 += - Dano_Total_sv2

                                            print("Tu deste",Dano_Total_sv2,"de dano")

                                            time.sleep(3)

                                    if HPsv2 < 0:

                                        ponto += 40
                                            
                                        dinheiros = [1,2,3]

                                        dinheiros1 = random.choice(dinheiros)

                                        match dinheiros1:
                                            case 1:
                                                print("Tu mataste o Siclop Anão com Gigantismo e ganhaste 34 moedas")

                                                dinheiro += 34

                                            case 2:
                                                print("Tu mataste o Siclop Anão com Gigantismo e ganhaste 33 moedas")

                                                dinheiro += 33

                                            case 3:
                                                print("Tu mataste o Siclop Anão com Gigantismo e ganhaste 35 moedas")

                                                dinheiro += 35
                                        
                                        break

                                case 2:

                                    if poções_de_cura < 0:
                                        
                                        print("Tu não tens poções de cura suficientes")

                                        time.sleep(3)

                                    else:

                                        poções_de_cura += -1

                                        HP += 30

                                        print("Tomaste uma poção de cura e curaste 30 de vida")

                                        time.sleep(3)

                                case 3: 

                                    print("O Siclop Anão com Gigantismo tem",HPsv2,"de Hp",ATKsv2,"de Atk e",Defsv2,"de Def")

                                    print("Este Siclop Anão com Gigantismo está seminu")

                                    time.sleep(10)
                                
                            print("O Siclop Anão com Gigantismo vai atacar")

                            Ataques = [1,2]

                            Ataque1 = random.choice(Ataques)

                            match Ataque1:
                                case 1:

                                    HP += -26

                                    print("O Siclop Anão com Gigantismo usou o ataque barte com borrete e deu 26 de dano")

                                case 2:

                                    HP += -21

                                    print("O Siclop Anão com Gigantismo usou o ataque olhar sigma 🗿🍷 e deu 21 de dano")

                            if HP < 0:

                                print("Tu morreste")

                                print("Tu tiveste",ponto,"ponto")
                                
                                exit()

                            print("Tu tens",HP,"de Hp e",poções_de_cura,"poções de cura")

            case 3:
                if i:
                    if i:

                        HPrv2 = 55

                        ATKrv2 = 28 or 24

                        Defrv2 = 5

                        while HP == HP:
                            
                            print("Qual será a tua ação?")

                            time.sleep(1)

                            ação = int(input("Atacar(1); Curar(2); Examinar(3): "))

                            time.sleep(1)

                            match ação:
                                case 1:
                                    dano = [1,2]

                                    dano1 = random.choice(dano)
                                    
                                    match dano1:
                                        case 1:

                                            Dano_Total_rv2 = -Defrv2 + ATK + 4

                                            HPrv2 += - Dano_Total_rv2

                                            print("Tu deste",Dano_Total_rv2,"de dano")

                                            time.sleep(3)

                                        case 2:
                                            Dano_Total_rv2 = -Defrv2 + ATK

                                            HPrv2 += - Dano_Total_rv2

                                            print("Tu deste",Dano_Total_rv2,"de dano")

                                            time.sleep(3)

                                    if HPrv2 < 0:

                                        ponto += 30
                                            
                                        dinheirorv2 = [1,2,3]

                                        dinheirorv21 = random.choice(dinheiror)

                                        match dinheirorv21:
                                            case 1:
                                                print("Tu mataste o Lobo Albino e ganhaste 39 moedas")

                                                dinheiro += 39

                                            case 2:
                                                print("Tu mataste o Lobo Albino e ganhaste 40 moedas")

                                                dinheiro += 40

                                            case 3:
                                                print("Tu mataste o Lobo Albino e ganhaste 41 moedas")

                                                dinheiro += 41
                                        
                                        break

                                case 2:

                                    if poções_de_cura < 0:
                                        
                                        print("Tu não tens poções de cura suficientes")

                                        time.sleep(3)

                                    else:

                                        poções_de_cura += -1

                                        HP += 30

                                        print("Tomaste uma poção de cura e curaste 30 de vida")

                                        time.sleep(3)

                                case 3: 

                                    print("O Lobo Albino tem",HPrv2,"de Hp",ATKrv2,"de Atk e",Defrv2,"de Def")

                                    print("O Lobo Albino tem dentes e unhas muito afiados")

                                    time.sleep(10)
                                
                            print("O Lobo Albino vai atacar")

                            Ataques = [1,2]

                            Ataque1 = random.choice(Ataques)

                            match Ataque1:
                                case 1:

                                    HP += -24 + Def

                                    print("O Lobo Albino usou o ataque mordida feroz e deu 24 de dano")

                                case 2:

                                    HP += -28 + Def

                                    print("O Lobo Albino usou o ataque unhas afiadas e deu 21 de dano")

                            if HP < 0:

                                print("Tu morreste")

                                print("Tu tiveste",ponto,"ponto")
                                
                                exit()

                            print("Tu tens",HP,"de Hp e",poções_de_cura,"poções de cura")

            case 4:
                print("Parece que apareceu um bau no canhinho")

                print("Qual a tua ação?")

                açaob = int(input("Abrir(1) ou passar longe(2): "))

                if açaob == 1:
                    açaob1 = [1,2]

                    açaob2 = random.choice(açaob1)

                    if açaob2 == 1:
                        print("O bau estava cheio de dinheiro")

                        print("Tu ganhaste 48 moedas")

                    else:
                        print("Afinal era um Mimico e ele está pronto para a batalha")

                        HPb = 70

                        ATKb = 30 or 35

                        Defb = 11

                        while HP == HP:
                            
                            print("Qual será a tua ação?")

                            time.sleep(1)

                            ação = int(input("Atacar(1); Curar(2); Examinar(3): "))

                            time.sleep(1)

                            match ação:
                                case 1:
                                    dano = [1,2]

                                    dano1 = random.choice(dano)
                                    
                                    match dano1:
                                        case 1:

                                            Dano_Total_b = -Defb + ATK + 4

                                            HPb += - Dano_Total_b

                                            print("Tu deste",Dano_Total_b,"de dano")

                                            time.sleep(3)

                                        case 2:
                                            Dano_Total_b = -Defb + ATK

                                            HPb += - Dano_Total_b

                                            print("Tu deste",Dano_Total_b,"de dano")

                                            time.sleep(3)

                                    if HPb < 0:

                                        ponto += 50
                                            
                                        dinheirorv2 = [1,2,3]

                                        dinheirorv21 = random.choice(dinheiror)

                                        match dinheirorv21:
                                            case 1:
                                                print("Tu mataste o Mimico e ganhaste 39 moedas")

                                                dinheiro += 50

                                            case 2:
                                                print("Tu mataste o Mimico e ganhaste 40 moedas")

                                                dinheiro += 49

                                            case 3:
                                                print("Tu mataste o Mimico e ganhaste 41 moedas")

                                                dinheiro += 48
                                        
                                        break

                                case 2:

                                    if poções_de_cura < 0:
                                        
                                        print("Tu não tens poções de cura suficientes")

                                        time.sleep(3)

                                    else:

                                        poções_de_cura += -1

                                        HP += 30

                                        print("Tomaste uma poção de cura e curaste 30 de vida")

                                        time.sleep(3)

                                case 3: 

                                    print("O Mimico tem",HPb,"de Hp",ATKb,"de Atk e",Defb,"de Def")

                                    print("O Mimico tem uma carapaça de bau muito resistente")

                                    time.sleep(10)
                                
                            print("O Mimico vai atacar")

                            Ataques = [1,2]

                            Ataque1 = random.choice(Ataques)

                            match Ataque1:
                                case 1:

                                    HP += -30 + Def

                                    print("O Mimico usou o ataque de lingua e deu 30 de dano")

                                case 2:

                                    HP += -35 + Def

                                    print("O Mimico usou o ataque Mordida de dinheiro e deu 35 de dano")

                            if HP < 0:

                                print("Tu morreste")

                                print("Tu tiveste",ponto,"ponto")
                                
                                exit()

                            print("Tu tens",HP,"de Hp e",poções_de_cura,"poções de cura")
