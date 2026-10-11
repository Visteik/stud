Size = int(input('Размер в Гб: '))
Speed = int(input('Скорость в Мбит/c: '))
Time1 = int(input("Ориентирвочное время в минутах: "))

All_time = (Size*1024*8)/Speed #время в секундах

Time_min = int(All_time//60)
Time_sec = int(All_time%60)
print("Выходные данные: ")
print("Время скачивание: ", Time_min, ":", Time_sec, sep='')
Sum_Time = Time_min + Time1
print("Общее время: ", Sum_Time, ":", Time_sec, sep='')