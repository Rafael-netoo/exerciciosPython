#somas dois hoários determinados e printa a hora resultante

from datetime import time, datetime, timedelta

def somaHora():
        #determina dois horários do tipo time
        time1 = time(hour=3, minute=45, second=0)
        time2 = time(hour=3, minute=20, second=0)

        #determina a data atual
        dataAtual = datetime.now()

        #determina um objeto do tipo datetime com o time1(3:45) e dataAtual
        data_e_hora1 = datetime.combine(dataAtual, time1)


        #atribui a variável data_e_hora3 a soma da data_e_hora1 com time2(14:45)
        data_e_hora3 = (data_e_hora1 + timedelta(hours=time2.hour, minutes=time2.minute, seconds=time2.second))

        if data_e_hora3.hour > 11:
            data_e_hora3  = timedelta(hours= data_e_hora3.hour - 12,minutes=data_e_hora3.minute, seconds=data_e_hora3.second)
        else:
            data_e_hora3 = timedelta(hours=data_e_hora3.hour,minutes=data_e_hora3.minute, seconds=data_e_hora3.second)
            print(data_e_hora3)


def SomaHoraAlternativo():
    h1 = int(input("Digite a primeira hora:"));
    m1 = int(input("Digite o primeiro minuto:"));
    h2 = int(input("Digite a segunda hora:"));
    m2 = int(input("Digite o segundo minuto:"));

    hora = h1 + h2
    minuto = m1 + m2

    if hora > 24:
        hora= hora-24
        if (minuto >= 60):
            hora = hora + 1
            minuto = minuto - 60

            if (hora >= 12):
                hora = hora - 12

                if (minuto < 10):
                    print(f"{hora}:0{minuto}")
                else:
                    print(f"{hora}:{minuto}")
            else:
                if (minuto < 10):
                    print(f"{hora}:0{minuto}")
                else:
                    print(f"{hora}:{minuto}")

        else:
            if (hora >= 12):
                hora = hora - 12

                if (minuto < 10):
                    print(f"{hora}:0{minuto}")
                else:
                    print(f"{hora}:{minuto}")

            else:
                if (minuto < 10):
                    print(f"{hora}:0{minuto}")
                else:
                    print(f"{hora}:{minuto}")

    if (minuto >= 60):
        hora = hora + 1
        minuto = minuto - 60

        if (hora >= 12):
            hora = hora - 12

            if (minuto < 10):
               print(f"{hora}:0{minuto}")
            else:
               print(f"{hora}:{minuto}")
        else:
            if (minuto < 10):
               print(f"{hora}:0{minuto}")
            else:
               print(f"{hora}:{minuto}")

    else:
        if (hora >= 12):
            hora = hora - 12

            if (minuto < 10):
                print(f"{hora}:0{minuto}")
            else:
                print(f"{hora}:{minuto}")

        else:
            if (minuto < 10):
               print(f"{hora}:0{minuto}")
            else:
               print(f"{hora}:{minuto}")


def horaAlternativa():
    h1 = int(input("Digite a primeira hora:"));
    m1 = int(input("Digite o primeiro minuto:"));
    h2 = int(input("Digite a segunda hora:"));
    m2 = int(input("Digite o segundo minuto:"));
    hora = h1 + h2
    minuto = m1 + m2
    if hora > 24:
        hora = hora - 24
    if hora > 12  :
        hora = hora - 12
    if minuto >= 60 :
        minuto = minuto - 60
        hora = hora + 1
    print(f"{hora}:{minuto}")
horaAlternativa()