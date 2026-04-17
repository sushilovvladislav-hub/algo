# Задание 6

# Сбор данных от пользователя
name = input("Введите Ваше имя: ")
age_str = input("Введите Ваш возраст: ")
subjects_str = input("Введите Ваши любимые предметы (через один пробел): ")

# Преобразование типов
age = int(age_str)
subjects_list = subjects_str.split()

# Создание словаря
student = {
    "name": name,
    "age": age,
    "favorite_subjects": subjects_list
}

# Вывод анкеты
print('=' * 30)
print("♥ АНКЕТА СТУДЕНТА ♥")
print('=' * 30)

print(f"Имя: {student["name"]}")
print(f"Возраст: {student["age"]}")
print(f"Любимые предметы: {student["favorite_subjects"]}")

print('=' * 30)
