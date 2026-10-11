x = input('Введите строку:')
print("Символов в строке:", len(x))
print("Байтов в UTF-8", len(x.encode('utf-8')))
print("Байтов в CP1251", len(x.encode('CP1251')))