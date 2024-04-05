#somas dois hoários determinados e printa a hora resultante

from datetime import time, datetime, timedelta
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