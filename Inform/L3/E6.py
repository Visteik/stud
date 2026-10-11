# Запрашиваем сообщение
message = input("Введите сообщение: ").strip()

# Проверяем, что строка не пустая
if message == "":
    print("Сообщение пустое. Пока.")
else:
    # Бесконечный цикл: меню показывается
    while True:
        # Выводим меню
        print("""
Меню:
1.  Проверить на палиндром
2.  Подсчитать гласные
3.  Проверить, только ли цифры
4.  Проверить, только ли буквы
5.  Перевернуть строку
6.  В верхний регистр
7.  В нижний регистр
8.  Заменить пробелы на "_"
9.  Проверить, похоже ли на email
10. Извлечь домен
11. Выход
""")

        # Запрашиваем выбор
        choice = input("Ваш выбор: ").strip()

        match choice:
            case "1":
                # Проверка на палиндром: игнорируем регистр и пробелы
                clean_message = ''.join(c for c in message if c.isalnum())
                
                clean_message_l = clean_message.lower()
                re_message = clean_message[::-1]
                re_message_l = re_message.lower()
                print(re_message_l)
                print(clean_message_l)
                if clean_message_l == re_message_l:
                    print("Это палиндром")
                else:
                    print("Не палиндром")

            case "2":
                # Подсчёт гласных (без учёта регистра)
                lower_msg = message.lower()
                count = (lower_msg.count("a") + lower_msg.count("e") +
                         lower_msg.count("i") + lower_msg.count("o") +
                         lower_msg.count("u"))
                print("Количество гласных:", count)
            case "3":
                # Проверить , только ли цифры
                if message.isdigit():
                    print("Только цифры")
                else:
                    print("Есть что-то кроме цифр")
            case "4":
                # Проверить, только ли буквы
                if message.isalpha():
                    print("Только буквы")
                else:
                    print("Есть что-то кроме букв")
            case "5":
                # Перевернуть строку
                reversed_message = message[::-1]
                print(reversed_message)
            case "6":
                # В верхний регистр
                up_message = message.upper()
                print(up_message)
            case "7":
                # В нижний регистр
                low_message = message.lower()
                print(low_message)
            case "8":
                # Заменить пробелы на "_"
                rep_message = message.replace(" ", "_")
                print(rep_message)
            case "9":
                # Проверить, похоже ли на email   
                idx = message.find("@")
                if idx == -1:
                    print("нет @")
                elif "." in message[idx +1:]:
                    print("Похож на email")
                else:
                    print("Не очень-то это email")
            case "10":
                # Извлечь домен
                idx = message.find("@")
                domen = message[idx+1:]
                print(domen)
            case "11":
                print("Выход. До связи).")
                break  # выходим из бесконечного цикла

            case _:
                print("Неверный выбор. Попробуйте ещё раз.")