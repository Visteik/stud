a = input()
b = ""
for i in a:
    if i.isalpha():
        b += i
    else:
        continue
print(b)