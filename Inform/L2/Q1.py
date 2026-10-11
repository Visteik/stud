a = int(input())
b = int(input())
c = int(input())
d = int(input())

left = max(a, c)
right = min(b, d)

if left < right:
    len1 = right - left
    print("[", left, ",", right, "] длина ", len1, sep="")
elif (left == right):
    print(left, "длина = 1")
else:
    print("Нет пересечений")