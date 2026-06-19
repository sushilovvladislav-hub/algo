print("Программа выводит список нечетных чисел от 1 до введенного числа пользователя")
num = int(input("Введите натуральное число: ")) + 1

odd_numbers = []

for i in range(1, num):
    if i % 2 != 0:
        odd_numbers += [i]

print(odd_numbers)
