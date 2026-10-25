depth = list(map(int, input("Введите список глубин через пробел: ").split()))
price_indx = []
price = []
for i in range(len(depth) - 1):
    if i != 0 and i != len(depth):
        if depth[i-1] < depth[i] and depth[i] < depth[i+1]:
            print(i, ". Индекс", i, ":", depth[i], ">", depth[i-1], depth[i], "<", depth[i+1], "= не сокровище")
        if depth[i+1] < depth[i] and depth[i] < depth[i-1]:
            print(i, ". Индекс", i, ":", depth[i], "<", depth[i-1], depth[i], ">", depth[i+1], "= не сокровище")
        if depth[i+1] > depth[i] and depth[i] < depth[i-1]:
            print(i, ". Индекс", i, ":", depth[i], "<", depth[i-1], depth[i], "<", depth[i+1], "= не сокровище")
        if depth[i-1] < depth[i] and depth[i] > depth[i+1]:
            price_indx.append(i)
            price.append(depth[i])
            print(i, ". Индекс", i, ":", depth[i], ">", depth[i-1], depth[i], ">", depth[i+1], "= сокровище")
print("Сокровища на индексах", ", ".join(map(str, price_indx)), "со значениями", ", ".join(map(str, price)))
big_price = max(price)
print("Самое глубокое", big_price)
depth.remove(big_price)
print(depth)