data = input("Введите данные в формате без пробелов: кол-во комнат/числоПроживающих числоМест/числоПроживающихN числоМестN ")
com = [p.strip() for p in data.split('/')]
print(com)
lud = com[1:]
print(lud)
count = 0
for i in lud:
    p, q = map(int, i.split())
    if q - p >=2:
        count += 1
print(count)