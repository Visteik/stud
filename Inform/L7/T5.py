nums = [12, -5, 0, 7, 18, -3, 9, 24, 6, 15]

chet_nums = list(filter(lambda x: x % 2 == 0, nums))
positive_nums = list(filter(lambda x: x > 0, nums))
num_3_5 = list(filter(lambda x: x % 3 == 0 and x > 5, nums))

print(f"Чётные: {chet_nums}")
print(f"Положительные: {positive_nums}")
print(f"Кратные 3 и >5: {num_3_5}")