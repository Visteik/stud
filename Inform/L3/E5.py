
from random import *

guess = randint(1, 100)

a = 0
while a != guess:
    a = int(input("Введите число "))
    if a > guess:
        print("Меньше")
    elif a < guess:
        print("Больше")
    else:
        print("Угадал!")