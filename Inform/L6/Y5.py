depth = input("Введите список глубин через пробел: ").split()
price_indx = []
price = []
for i in range(len(depth)):
    if i != 0 and i != len(depth) and 
        if depth[i-1] < depth[i] and depth[i] < depth[i+1]:
            print(i, ". Индекс" i, ":", depth[i], ">" depth[i-1], depth[i], "<" depth[i+1], "= не сокровище", sep='')
        if depth[i+1] < depth[i] and depth[i] < depth[i-1]
            print(i, ". Индекс" i, ":", depth[i], "<" depth[i-1], depth[i], ">" depth[i+1], "= не сокровище", sep='')
        if depth[i+1] > depth[i] and depth[i] < depth[i-1]
            print(i, ". Индекс" i, ":", depth[i], "<" depth[i-1], depth[i], "<" depth[i+1], "= не сокровище", sep='')
        if depth[i-1] < depth[i] and depth[i] > depth[i+1]:
            price_indx.append(i)
            price.append(depth[i])
            print(i, ". Индекс" i, ":", depth[i], ">" depth[i-1], depth[i], ">" depth[i+1], "= сокровище", sep='')
print("Сокровища на индексах", ", ".join(map(str, price_indx)), "со значениями", ", ".join(map(str, price)))
