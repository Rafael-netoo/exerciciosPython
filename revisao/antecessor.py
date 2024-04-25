def antecessor(valor):
     antecessor  =  valor - 1
     return antecessor

def sucessor(valor):
    sucessor  = valor + 1
    return sucessor

valor  =  int(input("Digite um valor:"))
antecessor = antecessor(valor)
sucessor = sucessor(valor)
print(f'O antecessor de {valor} é {antecessor} e e seu sucessor é {sucessor}')