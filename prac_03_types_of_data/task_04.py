# Задание 4

# Выбираем подходящий тип данных для переменных
cnt_of_students = 10    # int (целое число)
temp_in_cel = 23.5  # float (число с плавающей точкой)
user_login = "ivanov_ivan"  # string (строка)
is_notification_on = False  # bool (логический тип)
favorite_films = ["Whiplash", "Peaceful Warrior", "The Matrix"]    # list (список)
cords_of_dot = (1.0, 1.0)   # tuple (кортеж)
id_of_item = {101, 102, 103}    # set (множество)
country_to_capital = {"Russia": "Moscow", "Japan": "Tokyo", "Germany": "Berlin"}    # dictionary (словарь)

# Выводим переменные
print(f"Кол-во студентов (int): {cnt_of_students}")
print(f"Температура в градусах Цельсия (float): {temp_in_cel}")
print(f"Логин пользователя (string): {user_login}")
print(f"Информация о том, включено ли уведомление (bool): {is_notification_on}")
print(f"Список любимых фильмов (list): {favorite_films}")
print(f"Координаты точки в 2D пространстве (tuple): {cords_of_dot}")
print(f"Уникальные ID товаров в корзине покупок (set): {id_of_item}")
print(f"Соответствия между названием страны и её столицей (dict): {country_to_capital}")