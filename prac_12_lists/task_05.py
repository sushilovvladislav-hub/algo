data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
array_len = len(data)

first_three_nums = data[:3]
last_three_nums = data[array_len - 3:]
reverse_nums = data[::-1]
odd_nums = data[1::2]

print(f"Первая тройка чисел: {first_three_nums}")
print(f"Последняя тройка чисел: {last_three_nums}")
print(f"Список в обратном порядке: {reverse_nums}")
print(f"Список с элементами нечетных индексов: {odd_nums}")
