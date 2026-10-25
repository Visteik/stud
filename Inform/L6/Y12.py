data = input("Введите данные в формате без пробелов: ")
data_sort = [p.strip() for p in data.split('/')]
hod = data_sort[1].split()
n = data_sort[0]
print(n, hod)
x = 0
y = 0
for i in hod:
    if i == 'U':
        y += 1
    if i == 'D':
        y -= 1 
    if i == 'R':
        x += 1
    if i == 'L':
        x -= 1
res = abs(x) + abs(y)
print(x, y, "/", res)