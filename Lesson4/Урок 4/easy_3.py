# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
import random

count = 30

randlist = [random.randint(0,100) for _ in range(count)]
print(randlist)
randlist_new  = [i for i in randlist if i >= 0 and i % 3 == 0 and i % 4 != 0]
print(randlist_new)
