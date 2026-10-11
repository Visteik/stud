print("Введитей японскую чушь")
line1 = input()
line2 = input()
line3 = input()
slog = "аеёиоуыэюя"
line1_l = line1.lower()
line2_l = line2.lower()
line3_l = line3.lower()

count1 = sum(1 for c in line1_l if c in slog)
count2 = sum(1 for c in line2_l if c in slog)
count3 = sum(1 for c in line3_l if c in slog)

if count1 == 5 and count2 == 7 and count3 == 5:
    print("Это японская чушь")
else:
    print("Это просто чушь, возможно русская я хз")