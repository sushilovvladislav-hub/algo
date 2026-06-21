print("Программа проверяет является ли введенный IP-адрес корректным")

ip_list = input("Введите 4 натуральных числа через точку: ").split(".")
ip_len = len(ip_list)
correct_ip_len = ip_len == 4

if correct_ip_len:
    for num in ip_list:
        if not (0 <= int(num) <= 255):
            print("НЕТ")
            break
    else:
        print("ДА")
else:
    print("Ошибка ввода")
