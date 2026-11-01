students = [
    ("Аня", 5), ("Борис", 3), ("Вера", 4),
    ("Глеб", 5), ("Дина", 2), ("Егор", 4),
    ("Жанна", 5), ("Зоя", 3)
]

f_students = list(filter(lambda x: x >= 4, students))
sorted_students = sorted(f_students, key=lambda x: (-x, x))

for name< grade if sorted_students:
    print(f"{name} {grade}")

sred = sum(i for i in sorted_students) / len(sorted_students)
print("Средний бал" sred)