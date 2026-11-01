n, m = map(int, input("Введите кол-во рядов n и мест в ряду m через пробел: ").split())
rows = [list(map(int, input("введите данные о рядах").split())) for _ in range(n)]
k = int(input())

for i in range(n):
    count = 0
    for place in rows[i]:
        if place == 0:
            count += 1
            if count == k:
                print(i + 1)
                exit()
        else:
            count = 0

print(0)