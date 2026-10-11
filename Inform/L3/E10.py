print("Введите слово: ")
word = input()
res = ""
for c in word:
    if c.isupper():
        res += "_" + c.lower()
    else:
        res += c
print(res)