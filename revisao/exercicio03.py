anoAtual = 2024
mesAtual = 4
age = int(input('Digite a sua idade: '))
month = input('Digite o mês que você nasceu:')

if(month  == "s" or month =="S"):
    anoNascimento = anoAtual - age
else:
    anoNascimento = anoAtual - age - 1


print(f'Ano de nascimento : {anoNascimento}')