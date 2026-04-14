# Задание 2

number = int(input("Введите карман рулетки (от 0 до 36): "))

# Промежуток карманов на игровой рулетке
number_is_in_range = 0 <= number < 37

# Условия цветов карманов
number_is_green = number == 0



if not number_is_in_range:
    print("Вы ввели неправильный карман рулетки.")
else:
    print("Здесь надо написать много кода :( ")

