import random

def build_matr(n):
    square = [[0]*n for _ in range(n)]
    r = 0
    c = n//2
    for num in range(1, n*n + 1):
        square[r][c] = num
        next_r = (r - 1)%n
        next_c = (c + 1)%n
        if square [next_r][next_c] != 0:
            next_r = (r+1)%n
            next_c = c
        r, c = next_r, next_c
    return square

def rand_square(square):
    n = len(square)
    rows = list(range(n))
    cols = list(range(n))
    random.shuffle(rows)
    random.shuffle(cols)
    shuffled = [ [0]* n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            shuffled[i][j] = square[rows[i]][cols[j]]
    return shuffled

def magic(square):
    n = len(square)
    mconst = n*(n*n + 1)/2
    for r in range(n):
        if sum(square[r]) != mconst:
            return False
    for c in range(n):
        if sum(square[r][c] for r in range(n)) != mconst:
            return False
    if sum(square[r][r] for r in range(n)) != mconst:
        return False
    if sum(square[r][n - 1 - r] for r in range(n)) != mconst:
        return False
    return True



n = int(input("Введите N: "))
if n%2 == 0:
    print("N должен быть нечётным.")
    exit()

base_square = build_matr(n)
new_square = rand_square(base_square)
for i in new_square:
    print(i)
magic_const = n * (n * n + 1) / 2
if magic(new_square):
    print("Проверка пройдена: все суммы совпадают.")
else:
    print("Ошибка: суммы не совпадают.")


