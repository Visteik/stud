All_T = int(input('Кол-во товара: '))
Vmest = int(input('Вместимость: '))

x = int(All_T/Vmest)
y = All_T - x*Vmest
z = (1- y/All_T)*100
print("Выходные данные: ")
print("Полных контейнеров: ", x)
print("Остаток товара: ", y)
print("эффективность: ", round(z, 2), "%", sep='')