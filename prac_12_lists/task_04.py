marks = [5, 4, 3, 5, 2, 5, 4, 3, 5, 5]

fives_cnt = 0
twos_cnt = 0

for mark in marks:
    if mark == 5:
        fives_cnt += 1
    elif mark == 2:
        twos_cnt += 1

print(f"Количество пятерок: {fives_cnt}")
print(f"Количество двоек: {twos_cnt}")
