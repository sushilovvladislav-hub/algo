from random import randint

print("Программа обменивает местами первый элемент и минимальный элемент списка с 5 случайными числами")
random_list = [randint(-255, 255), randint(-255, 255), randint(-255, 255), randint(-255, 255), randint(-255, 255)]
print(random_list)

min_index = 0
min_elem = min(random_list)
random_list_len = len(random_list)


for i in range(random_list_len):
    if random_list[i] == min_elem:
        min_index = i
        break

random_list[0], random_list[min_index] = random_list[min_index], random_list[0]
print(random_list)
