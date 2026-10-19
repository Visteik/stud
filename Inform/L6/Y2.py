price = input("Введите кол-во проданных через пробел: ").split()
price = list(map(int, price))
price_g = []
for i in range(len(price)):
    if price[i] > price[i-1]:
        price_g.append(price[i])
print(" ".join(map(str, price_g)))