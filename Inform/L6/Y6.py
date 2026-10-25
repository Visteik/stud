card = input("Введите номер карты без пробелов: ")
card_numbers = [int(d) for d in card]
print(card_numbers)
sum_chet = 0
sum_nechet = 0
for i in range(len(card_numbers)):
    if (i+1) % 2 != 0:
        temp = card_numbers[i]*2
        if temp > 9:
            temp -= 9
        sum_nechet += temp
    elif (i+1) % 2 == 0:
        sum_chet += card_numbers[i]
        
print(sum_chet, sum_nechet)
res = sum_nechet + sum_chet
print(res)
if res%10 == 0:
    print("Корректный номер")
else:
    print("Некорректный номер")
