prices = [1500, 500, 2000, 3500, 1000, 4500]

most_exp_item = max(prices)
most_cheap_item = min(prices)
total_sum = sum(prices)
avg_price = total_sum / len(prices)

print(f"Самый дорогой товар стоит {most_exp_item}")
print(f"Самый дешевый товар стоит {most_cheap_item}")
print(f"Общая стоимость всех товаров: {total_sum}")
print(f"Средняя цена товаров: {avg_price: .1f}")
