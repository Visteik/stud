letter1 = input("Буква начальной: ")
b = int(input("Номер начальной: "))
letter2 = input("Буква конечной: ")
d = int(input("Номер конечной: "))

if ( ord("a") < ord(letter1) < ord("h") and ord("a") < ord(letter2) < ord("h") and 1 < b < 8 and 1 < d < 8):
    print("Неверный ввод")
elif (abs(b - d) == abs(ord(letter1) - ord(letter2)) or abs(b + d) == abs(ord(letter1) + ord(letter2))):
    print("YES")
else:
    print("NO")