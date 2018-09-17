# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
import random

count = 30

randlist = [random.randint(-100,100) for _ in range(count)]
print(randlist)
randlist_new  = [i for i in randlist if i >= 0 and not i % 3 and i % 4]
print(randlist_new)
