n, k = map(int, input("Введите данные в формате без пробелов: ").split())
people = list(range(1, n+1))
print(people)
cickle = []
idx = 0
while len(people) > 0:
    idx = (idx + k - 1) % len(people)
    cickle.append(people.pop(idx))
print(*cickle[:-1], '/', cickle[-1])