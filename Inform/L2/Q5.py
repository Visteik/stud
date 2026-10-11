a = int(input("Расстояние: "))
b = int(input("Скорость: "))

if 0 <= a < 0.1 and 0 <= b < 100:
    print ("WIFI")
elif 0 <= a < 10 and 0 <= b < 150:
    print ("LTE")
elif 0 <= a < 2 and 0 <= b < 1000:
    print ("5G")
elif 0 <= a < 1000 and 0 <= b < 200:
    print ("SATELLITE")
else:
    print("Пора покинуть землю")