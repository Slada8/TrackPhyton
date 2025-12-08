money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
money_rest = money_capital
i = 0
while money_rest >= 0:
    i += 1
    money_rest = money_rest + salary - spend * (1 + increase) ** i
print("Количество месяцев, которое можно протянуть без долгов:", i)
