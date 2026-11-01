import math

n = int(input("введите кол-во скоровищ "))
if n < 1:
    print("Нет сокровищ.")
else:    
    treasures = []
    for i in range(n):
        x, y = map(int, input("Введите х у сокровищ через пробел ").split())
        treasures.append((x, y))

    ax, ay = map(int, input("введите координаты сани").split())
    mx, my = treasures[0]
    min_dist = math.sqrt((mx - ax)**2 + (my - ay)**2)
    min_treasure = (mx, my)
    for x, y in treasures:
        dist = math.sqrt((x - ax)**2 + (y - ay)**2)
        if dist < min_dist:
            min_dist = dist
            min_treasure = (x, y)

    print(f"Ближайшее сокровище: {min_treasure[0]} {min_treasure[1]}")
    print(f"Расстояние: {min_dist:.2f}")