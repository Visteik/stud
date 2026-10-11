print("Введите зашифрованное слово: ")
word_s = input()

if word_s.endswith("#"):
    word = word_s[:-1]
    left_part = word[::2]
    right_part_r = word[1::2]
    right_part = right_part_r[::-1]
    print(left_part + right_part)

else: 
    print("Ошибка!! нет #")