# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

import random

count = 10

randlist = [random.randint(0,100) for _ in range(count)]
print(randlist)
randlist_new = [i ** 2 for i in randlist]
print(randlist_new)