vetorA = [0,0,0,0,0,0,0,0,0,0]
vetorM = [0,0,0,0,0,0,0,0,0,0]
for k in range(len(vetorA)):
    vetorA[k] = float(input(f'Digite o {k}º número:'))

x = float(input("Digite um número:"))

for y in range(len(vetorM)):
    vetorM[y] = vetorA[y]*x

for i in range(len(vetorM)):
    print(vetorM[i])