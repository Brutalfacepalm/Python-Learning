# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
import random

randlist = []

i = 0
while i < random.randint(1,50):
    randlist.append(random.randint(-100,100))
    i += 1
print (randlist)