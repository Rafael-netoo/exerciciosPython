resposta ='S'
while (resposta == 'S' or resposta =='s'):
    numero  = int(input("Digite um número:"))

    if(numero>0):
        print(f'{numero} é positivo!')
    else:
        print(f'{numero} é Negativo!')
    resposta = (input("Deseja avaliar um número novamente(S/s para sim - Qualquer tecla para não)?"))