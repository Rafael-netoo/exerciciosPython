print("Digite algumas informações eleitorias do seu município:")
eleitores = int(input("Digite o nº de eleitores que votaram :"))
brancos = int(input("Digite o nº de votos brancos : "))
nulos  = int(input("Digite o nº de votos nulos: "))
validos = int(input("Digite o nº de votos válidos: "))

P_brancos = (brancos * 100)/eleitores
P_nulos = (nulos *100)/eleitores
P_validos = (validos * 100)/eleitores

print("Percentuais :")
print(f"Validos: {P_validos}%")
print(f"Nulos: {P_nulos}%")
print(f"Brancos: {P_brancos}%")