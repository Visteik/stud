a = int(input("Первый: "))
b = int(input("Второй: "))
c = int(input("Третий: "))
d = int(input("Четвертый: "))

if a == 1 and d == 1:
    print("CLOSED")
elif a == 1 and b == 0:
    print("OPEN")
elif c == 1 and d == 1:
    print("OPEN")
else:
    print("CLOSED")