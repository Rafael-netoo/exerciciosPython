#recebe nomes e gols de dois times e retorna vencedor ou empate
time1 = input("Digite o nome do primeiro time: ")
gols1 = int(input("Digite o número de gols do primeiro time: "))
time2 = input("Digite o nome do segundo time: ")
gols2 = int(input("Digite o número de gols do segundo time: "))

if gols1 > gols2:
  print(time1, "venceu")
elif gols1 == gols2:
  print("Empate")
else :
  print(time2, "venceu !")