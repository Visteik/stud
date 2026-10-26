def func(x):
    return x ** 2 / 10 + 1
N = 10
for g in range(4):
    # Отрезок и число разбиений
    a, b = -2, 5

    # Шаг сетки
    h = (b - a) / N

    # Вычисляем значения функции в точках сетки
    values = []
    for i in range(N):
        x_i = a + i * h
        values.append(func(x_i))

    # Суммируем площади прямоугольников
    S = (func(a)+func(b))*h/2
    for v in values:
        S += v * h

    print(f"S = {S:.2f}", "N= ", N)
    N *= 10