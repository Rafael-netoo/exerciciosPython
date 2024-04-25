soma  = 0 ;
nota = -1
for x in range(2):
    nota = float(input(f'Digite a nota{x+1}:'))
    while(nota < 0 or nota >10):
        print("Digite uma nota válida!")
        nota = float(input(f'Digite a nota {x+1} novamente : '))
    soma  = soma + nota

media  = soma/2
print(f' Média:{media}')
