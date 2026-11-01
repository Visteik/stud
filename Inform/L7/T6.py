words = ["яблоко", "кот", "программирование", "дом", "молоко"]
students = [("Аня", 20), ("Борис", 18), ("Вера", 22), ("Глеб", 19)]
nums = [33, 12, 45, 21, 8, 99]

sorted_words = sorted(words, key=lambda x: len(x))
sorted_students = sorted(students, key=lambda x: x)
sorted_nums = sorted(nums, key=lambda x: x % 10)

print(sorted_words)
print(sorted_students)
print(sorted_nums)