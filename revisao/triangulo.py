def triangulo(base, altura):
    area = base*altura/2
    return area

def quadrado(lado):
    area  = lado**2
    return area

baseT  = float(input("Digite o valor da base do triangulo(cm):"))
alturaT = float(input("Digite o valor d altura do triangul(cm):"))

ladoQ = float(input("Digite a medida do lado do quadrado(cm): "))

areaT = triangulo(baseT,alturaT)
areaQ  = quadrado(ladoQ)

print(f'A área do triangulo : {areaT} cm²')
print(f'A área do quadrado : {areaQ}')