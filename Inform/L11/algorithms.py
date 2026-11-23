"""Модуль с реализацией базовых алгоритмов по блок-схемам."""


def reverse_number(n):
    """Возвращает целое число с цифрами в обратном порядке.
    Принимает целое неотрицательное число и возращает его с ццифрами в обратном порядке """
    if n == 0:
        return 0
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10

    return rev


def gcd(a, b):
    """Возвращает наибольший общий делитель чисел a и b.
    Принимает два числа и возращает наибольший общий делитель"""
    if a == 0:
        return b
    if b == 0: 
        return a

    while b != 0:
        temp = b
        b = a%b
        a = temp
    return a

def is_prime(n):
    """Проверка числа 'n' на простоту, Возвращает True или False"""
     
    
    if n <= 1:
        return False
    d = 2
    while d*d <= n:
        if n%d == 0:
            return False
        d += 1
    return True

def fibonacci(n):
    """N-е число Фибоначчи 
    Числовую последовательность размерности "n" в которой первые два числа равны 0 и 1,
    а каждое последующее число равно сумме двух предыдущих."""
    if n == 0:
        return 0
    prev = 0
    curr = 1
    i = 1
    while i < n:
        nxt = prev + curr
        prev = curr
        curr = nxt
        i = i + 1
    return curr

def max_increasing_len(arr):
    """Наибольшая последовательность возрастающих элементов
    функция принимает список чисел arr 
    и находит максимальную длину непрерывного строго возрастающего подотрезка (arr[i] > arr[i - 1])
    Возвращает длину"""
    if len(arr) == 0:
        return 0
    cur = 1
    best = 1
    i = 1
    while i < len(arr):
        if arr[i] > arr[i-1]:
            cur = cur + 1
        else:
            cur = 1
        best = max(best, cur)
        i += 1
    return best

def sqrt_newton(n, eps=1e-6):
    """Квадратный корень методом Ньютона (Герона)
    ВОзвращает приближенное значение корня неотрицательного числа 'n' с точностью eps"""

    if n == 0:
        return 0
    x = n /2
    while abs(x*x-n) > eps:
        x = 0.5 * (x + n / x)
    return x

def second_max(arr):
    """Поиск второго максимума
    Принимает список чисел "arr" и возвращает второй по величине элемент в списке"""
    if len(arr) < 2:
        return None
    m1 = float('-inf')
    m2 = float('-inf')
    i = 0
    while i < len(arr):
        if arr[i] > m1:
            m2 = m1
            m1 = arr[i]
        elif m2 < arr[i] < m1:
            m2 = arr[i]
        i = i + 1
    return m2

def count_primes_up_to(n):
    """Количество простых чисел в диапазоне от 2 до N
    Принимает число "n" 
    Возвращает число простых чисел в промежутке от 2 до n"""
    cnt = 0
    num = 2
    while num <= n:
        is_p = True
        d = 2
        while d*d <= num and is_p:
            if num % d == 0:
                is_p = False
            d = d + 1
        else:
            if is_p:
                cnt = cnt + 1
            num = num + 1
    return cnt