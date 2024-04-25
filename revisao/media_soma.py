def media():
    valor = 0
    for x in range(4) :
        numero = float(input(f'Digite o {x + 1} º número :'))

        valor = numero + valor
    media  = valor/4
    return media

def soma():
    valor = 0
    for x in range(4) :
        numero = float(input(f'Digite o {x + 1}º número :'))
        valor = numero + valor
    return valor


while True:

    print("Qual calculo/operação voce deseja fazer ?")
    print("1 - Soma", " ", "2 - Média" ," " ," 3 - Sair")
    opcao = int(input("Digite a opção : "))

    if(opcao == 1):
        Soma = soma()
        print(f'Resultado da Soma: {soma}')
    elif(opcao == 2):
        media  = media()
        print(f'Resultado da média: {media}')
    elif(opcao == 3):
        print("Programa encerrado!3")
        break
    else:
        print("Opção inválida !!!")   
