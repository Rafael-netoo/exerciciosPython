class Produto:
    def __init__(self, nome, qtd, valor):
        self.nome = nome
        self.qtd = qtd
        self.valor = valor

def tamanho(y):
    contador = 0
    for x in range(len(y)):
        contador+=1
    return contador

def vogais(y):
 contador = 0
 vogais = "aeiouAEIOU"
 for x in y:
    if x in vogais:
         contador +=1
 return contador

def space(y):
 contador = 0
 for x in range(len(y)):
     if(y[x] == " "):
         contador +=1

 return contador

def valorTotal(produto,qtd,valor):
    total  = qtd*valor

    return total

def sinal(x):
    sinal = " "
    if(x > 0):
        sinal = "P"
    elif(x < 0):
        sinal = "N"
    else:
        sinal = "Z"

    return sinal