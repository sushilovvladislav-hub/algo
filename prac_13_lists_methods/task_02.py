number = int(input("Введите натуральное число (кол-во строк): "))
res_list = []

for _ in range(number):
    string = input("Введите строку: ")
    res_list.extend(string)

print(res_list)
