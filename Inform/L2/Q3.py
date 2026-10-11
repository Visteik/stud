a = int(input("минуты парковки"))
b = int(input("Час въезда"))

cost = 0
if 22 <= b < 24 or 0 <= b < 6:
    if 30 <= a < 120:
        cost = 1.2*100
        print(cost)
    elif 120 <= a < 300:
        cost = 1.2*250
        print(cost)
    elif 300 <= a:
        cost = 1.2*500
        print(cost)
    else:
        print(cost)
elif b >= 24:
    print("ТЫ с земли?")
else:
    if 30 <= a < 120:
        cost = 100
        print(cost)
    elif 120 <= a < 300:
        cost = 250
        print(cost)
    elif 300 <= a:
        cost = 500
        print(cost)
    else:
        print(cost)