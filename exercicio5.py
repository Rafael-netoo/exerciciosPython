#algoritmo recebe o tipo de combustivel e quantidade de litros e retorna valor total.

litros = float(input("Digite a quantidade de litros:"))
combustivel = input("Digite o tipo de combustível (E-Etanol, G-Gasol):")

precoE = 4.9
precoG = 5.8

if combustivel == "E" or combustivel == "e"  :
   valor = litros*precoE
   print (f"Você irá pagar R$ {valor:,.2f}")
elif combustivel == "G" or combustivel == "g"  :
   valor  = litros*precoG;
   print(f"Você irá pagar R$  {valor:,.2f}")
else:
  print("Combustível inválido")