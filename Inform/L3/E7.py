email = input("Введите email: ")
password = input("Введите пароль: ")

email_otchet = []
password_otchet = []

if email.count("@") > 1:
    email_otchet.append("х Слишком много @")

idx = email.find("@")
if not "." in email[idx +1:]:
    email_otchet.append("х Нет точки после @")

if email.startswith("."):
    email_otchet.append("х Начинается на точку")
elif email.startswith("@"): 
    email_otchet.append("х Начинается на @")
elif email.endswith("."): 
    email_otchet.append("х Заканчивается на точку")
elif email.endswith("@"): 
    email_otchet.append("х Заканчивается на @")

if len(email) < 6 :
    email_otchet.append("х Слишком мало символов")
elif len(email) > 30:
    email_otchet.append("х Слишком много символов")

if len(password) < 8:
    password_otchet.append("х Слишком короткий пароль")

if password.isdigit == -1:
    password_otchet.append("х Нет цифр")

if not any("A" <= c <= "Z" for c in password): # c это любая перменная можно обзывать как хочешь.
    password_otchet.append("х Нет заглавной буквы")

if not any("a" <= c <= "z" for c in password): # c это любая перменная можно обзывать как хочешь.
    password_otchet.append("х Нет строчной буквы")

spec = "!@#$%^&*"
if not any(c in spec for c in password): # c это любая перменная можно обзывать как хочешь.
    password_otchet.append("х Нет спец символа")    

if email_otchet == "":
    print(email, "OK")
else:
    print(email, "NOT OK")
    for i in email_otchet:
        print(i)
if password_otchet == "":
    print(password, "OK")
else:
    print(password, "NOT OK ")
    for i in password_otchet:
            print(i)