# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()
lenght = 0
max_lenght = 0

fruits = ["яблоко", "банан", "киви", "арбуз", "авокадо", "крыжовник", "сладкий бубалех"]

for fruit in fruits:
    lenght = len(fruit)
    if max_lenght < lenght:
        max_lenght = lenght
    else:
        pass

for number, fruit in enumerate(fruits, start=1):
    fruit = fruit.rjust(max_lenght)
    print ('{}. {}'.format(number, fruit))