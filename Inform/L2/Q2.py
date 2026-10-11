a = int(input())
b = int(input())
c = int(input())
d = int(input())

left = max(a, c)
right = min(b, d)

if left < right:
    print("YES")
else:
    print("NO")