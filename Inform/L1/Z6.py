a = input('Введите строку:  ')
print(a.encode('utf8'))
b = a.encode('utf8')
print(b.decode('CP1251'))
c = b.decode('CP1251')

c = c.encode('CP1251')

print(c.decode('utf8'))