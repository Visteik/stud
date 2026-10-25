data = input("Введите данные в формате без пробелов: ")
data_sort = [p.strip() for p in data.split('/')]
chisla = data_sort[1].split()
hod = data_sort[0]
print(chisla, hod)

n, k = map(int, hod.split())

k %= n
print(k)
if k == 0:
    res = chisla
else:
    res = chisla[n-k:] + chisla[:n-k]
print(*res)

