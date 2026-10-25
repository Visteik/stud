import random
monet = []
count = 0
while True:
    monet.append(random.choice(['О', 'Р']))     
    count += 1
    if len(monet) >= 3 and monet[-1] == monet[-2] == monet[-3]:
     break
print("Последовательность:", ''.join(monet))
print("Количество бросков:", count)

