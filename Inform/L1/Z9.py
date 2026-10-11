number = input("Введите номер автомобиля:")
a = len(number)
if a == 6 and number[:3].isalpha() and number[3:].isdigit():
    print("Старый")
elif a == 7 and number[:3].isalpha() and number[4:].isdigit():
    print("Новый")
else:
    print("несоотвествует")