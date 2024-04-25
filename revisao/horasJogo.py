print("Digite os horários do jogo:")
hora1 = int(input("Início :"))
hora2 = int(input("Fim : "))

if(hora1 > hora2):
    duracao = (24 - hora1) + hora2
else:
   duracao = hora2 - hora1

print(f"A partida durou {duracao} horas.")