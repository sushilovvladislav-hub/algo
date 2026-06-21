print("Программа выводит кол-во пар элементов, равных друг другу")

nums_list = input("Введите целые числа через пробел: ").split()
pairs = 0

for i in range(len(nums_list)):
    for j in range(i + 1, len(nums_list)):
        if nums_list[i] == nums_list[j]:
            pairs += 1

print(f"Кол-во пар в списке {pairs}")
