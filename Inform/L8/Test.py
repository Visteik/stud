import matplotlib.pyplot as plt

# Простые данные для проверки
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Строим график
plt.plot(x, y, marker='o', color='b')
plt.title("Проверка Matplotlib")
plt.xlabel("Ось X")
plt.ylabel("Ось Y")
plt.grid(True)

plt.show()