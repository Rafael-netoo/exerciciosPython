array  = [0,0,0,0,0]

for x in range(len(array)):
    array[x] = int(input("Digite um número:"))

for y in range(len(array)-1,-1,-1):
    print(f"{array[y]}")