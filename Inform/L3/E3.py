chis = int(input())
n = 0

for i in range(1, chis + 1):
    str_chis = str(i)
    d = len(str_chis)
    sum = 0
    for j in str_chis: 
        sum += int(j)**d
    if (sum == i):
        n += 1
print(n)