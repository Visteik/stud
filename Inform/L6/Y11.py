grades = [" 5 ", "неявка", "4", " хор ", "", "100", "2", "два"]
grades = [i.strip().lower() for i in grades]
spis_sort = ['2', '3', '4', '5', 'уд', 'хор', 'отл', 'неуд', 'два', 'три', 'четыре', 'пять']
grades = [g for g in grades if g in spis_sort]
print(grades)
for idx, i in enumerate(grades):
    if i == 'неуд' or i == 'два':
        grades[idx] = '2'
    if i == 'уд' or i == 'три':
        grades[idx] = '3'
    if i == 'хор' or i == 'четыре':
        grades[idx] = '4'
    if i == 'отл' or i == 'пять':
        grades[idx] = '5'
print(grades)
grades = list(map(int, grades))
grades.sort(reverse=True)
print(grades)