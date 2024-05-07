estudantes = ["","","","",""]

for x in range (len(estudantes)):
    estudantes[x] = input(f"Digite o nome do {x+1}º estudante:")

for y in range (len(estudantes)):
    print(f"estudante {y}: {estudantes[y]}")