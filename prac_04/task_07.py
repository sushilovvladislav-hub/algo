# Задание 7

SEATS_PER_COMPARTMENT = 4   # кол-во мест в купе

# Вводим номер места
seat_num = int(input("Введите номер места: "))

# Считаем номер купе по месту
compartment_num = (seat_num - 1) // SEATS_PER_COMPARTMENT + 1

# Вывод
print("compartment_num")
