a = int(input("Первый октет: "))
b = int(input("Второй октет: "))
c = int(input("Третий октет: "))
d = int(input("Четвертый октет: "))

if 0 <= a <= 255 and 0 <= b <= 255 and 0 <= c <= 255 and 0 <= d <= 255:
    if a == 0 and b == 0 and c == 0 and d == 0:
        print("UNSPECIFIED")
    elif a == 127 and b == 0 and c == 0 and d == 1:
        print("LOOPBACK")
    elif 224 <= a <= 239:
        print("MULTICAST")
    elif a == 10:
        print("PRIVATE")
    elif a == 172 and 16 <= b <= 31:
        print("PRIVATE")
    elif a == 192 and b == 168:
        print("PRIVATE")
    else:
        print("PUBLIC")
else:
    print("INVALID")