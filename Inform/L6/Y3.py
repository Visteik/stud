stroy = input("Введите рост в строю через пробел: ").split()

andrey = input("Введите рост андрея ")
stroy.append(andrey)
stroy.sort()
print(" ".join(map(str, stroy)))
indx = len(stroy) - 1 - stroy[::-1].index(andrey)
print(indx + 1)