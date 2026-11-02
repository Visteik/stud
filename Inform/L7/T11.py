def window(lst, window_size):

    result = [tuple(lst[i:i + window_size]) for i in range(len(lst) - window_size)]
    return result


window_size = int(input("Введите длину окна: "))
lst = list(map(int, input("Введите список: ").split()))
windows = window(lst, window_size)
print(windows)