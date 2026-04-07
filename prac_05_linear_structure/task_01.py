# Задание 1

TAX_RATE = 13.0   # процентная ставка от дохода

# Ввод данных
total_income = float(input("Введите ваш годовой доход: "))

# Считаем доход после вычета налога
tax_share_of_income = total_income * TAX_RATE / 100.0
income_after_tax = total_income - tax_share_of_income

# Вывод
print(f"Ваш доход при процентной ставке подоходного налога {TAX_RATE}% равен {income_after_tax:.2f} рублей")