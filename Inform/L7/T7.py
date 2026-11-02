students = [
    ("Аня", 5), ("Борис", 3), ("Вера", 4),
    ("Глеб", 5), ("Дина", 2), ("Егор", 4),
    ("Жанна", 5), ("Зоя", 3)
]

f_students = list(filter(lambda x: x[1] >= 4, students))
sorted_students = sorted(f_students, key=lambda x: (-x[1], x[0]))

for name, grade in sorted_students:
    print(f"{name} {grade}")

sred = sum(i[1] for i in sorted_students) / len(sorted_students)
print("Средний бал", sred)