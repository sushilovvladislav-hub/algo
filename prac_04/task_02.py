# Задание 2

import math

def calc_euclidean_distance(x1, y1, x2, y2):
    """ Функция высчитывает эвклидово расстояние между двумя точками через их координаты"""
    euclid_distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return euclid_distance

# Ввод данных
cord_x1, cord_y1 = map(float,(input("Введите координаты первой точки в формате (x y): ")).split())
cord_x2, cord_y2  = map(float,(input("Введите координаты второй точки в формате (x y): ")).split())


print(f"Евклидово расстояние между двумя точками равно {calc_euclidean_distance(cord_x1,cord_y1,cord_x2,cord_y2):.2f} мат. ед.")
