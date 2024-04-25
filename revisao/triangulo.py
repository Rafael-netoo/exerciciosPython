def triangulo():
    while True:
        baseT  = float(input("Digite o valor da base do triangulo(cm):"))
        alturaT = float(input("Digite o valor d altura do triangul(cm):"))

        if(baseT < 1 or alturaT < 1):
            print ("Medida(s) inválida(s), digite um valor válido!")
        else:
            area = baseT*alturaT/2
            break
    return area

def quadrado():

    while True:
        ladoQ = float(input("Digite a medida do lado do quadrado(cm): "))
        if ( ladoQ < 1):
         print ("Medida inválida, digite um valor válido!")
        else:
            area  = ladoQ**2
            break
    return area

while True:

    print("Qual calculo/operação voce deseja fazer ?")
    print("1 - Triângulo", " ", "2 - Quadrado" ," " ," 3 - Sair")
    opcao = int(input("Digite a opção : "))

    if(opcao == 1):
        areaT = triangulo()
        print(f'A área do triangulo : {areaT} cm²')
    elif(opcao == 2):
        areaQ  = quadrado()
        print(f'A área do quadrado : {areaQ}')
    elif(opcao == 3):
        print("Programa encerrado!3")
        break
    else:
        print("Opção inválida !!!")