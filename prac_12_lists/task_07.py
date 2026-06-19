print("Программа выводит индекс введенного числа, если оно есть в списке")

numbers = [10, 20, 30, 40, 50]
numbers_len = len(numbers)
target = int(input("Введите число: "))

for i in range(numbers_len):
    if numbers[i] == target:
        print(f"Индекс числа {target} равен {i}")
        break
else:
    print("Нет такого числа")
