nomes = ["","","","",""]
senhas = ["","","","",""]
x = "0"
while (x == 1 or x == 2 or x =="0"):
    print("Escolha uma opção:")
    print("1 - Cadastro")
    print("2 - Login")
    x = input("Opção: ")

    if (x == "1"):
        for x in range(len(nomes)):

            print("\n")
            nomes[x] = input("Digite o nome do usuário:")
            senhas[x] = input("Digite a senha do usuário:")

        for y in range (len(nomes)):
            print("\n")
            print(f"Usuario posição [{y}]:")
            print(f"Nome : {nomes[y]}")
            print(f"Senha : {senhas[y]}")

    else:
        nome = input("Digite o nome do usuário:")
        senha = input("Digite a senha:")
        posicao = 0
        existe = 0
        for k in range(len(nomes)):
         if(nomes[k] == nome):
            posicao = k
            existe +=1
        if (senhas[posicao] == senha and existe == 1):
            print("Login realizado com sucesso")
            print(f"Nome : {nomes[posicao]}")
            print(f"Senha : {senhas[posicao]}")

        elif (existe==0):
         print("usuário não encontrado")
        elif(senhas[posicao] != senha):
         print("Senha incorreta")
        else:
          print("Usuário ou senha errados!")

