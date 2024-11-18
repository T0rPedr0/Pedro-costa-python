turma = []

for var in range (3):

    pessoa = input("Qual o nome do aluno: ")

    turma.append (pessoa)

print("A turma tem o/a",turma)

num = int(input("Diz um numero de 0 a 2: "))

if num > 3 or num < 0:
    print ("A posição tem de ser entre 0 e 2")

else:
    print("o aluno escolhido foi o/a",turma[num])
