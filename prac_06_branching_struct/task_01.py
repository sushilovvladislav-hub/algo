# Задание 1

temp, pressure, pulse = map(int, input("Введите температуру, давление и пульс через пробел: ").split())

# Прописываем условия, когда параметры являются симптомом легкого недомогания
temp_condition_easy = (35 <= temp < 36) or (37 <= temp < 38)
pressure_condition_easy = (105 <= pressure < 110) or (130 <= pressure < 140)
pulse_condition_easy = (55 <= pulse < 60) or (100 <= pulse < 110)

# Прописываем условия, когда параметры в критических зонах
temp_condition_critical = temp < 35 or temp > 38
pressure_condition_critical = pressure < 105 or pressure > 140
pulse_condition_critical = pulse < 55 or pulse > 110

if temp_condition_easy or pressure_condition_easy or pulse_condition_easy:
    print("У вас легкое недомогание, пожалуйста проследуйте на обследование.")
elif temp_condition_critical or pressure_condition_critical or pulse_condition_critical:
    print("Ваша жизнь под угрозой! Немедленно проследуйте на обследование!")
else:
    print("Вы в полном порядке :)")
