numero = [0,0,0]
for x in range(3):
    numero[x] = int(input("Digite um número: "))

if(numero[0] > numero[1]):
    if(numero[0] > numero[2]):
        print(f'O maior número é :{numero[0]}')
    else:
        print(f'O maior número é: {numero[2]}')
else:
    if(numero[1] > numero[2]):
        print(f'O maior número é :{numero[1]}')
    else:
        print(f'O maior número é: {numero[2]}')