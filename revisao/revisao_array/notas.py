notas  = [0,0,0,0,0]
somador = 0
contador = 0
for x in range(len(notas)):
    notas[x] = float(input(f"Digite a nota do {x+1}º estudantes :"))
    somador  = notas[x] + somador

media  = somador/len(notas)

for y in range(len(notas)):
    if(notas[y]>= media):
        contador +=1

print(f"A média da turma é {media} e {contador} estão acima da média")


