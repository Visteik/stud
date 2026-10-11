text = input()
word = input()
k = 0
for i in word:
    if k < len(word) and i == text[k]:
        k += 1

print(k == len(word))

