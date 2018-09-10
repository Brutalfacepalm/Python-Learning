# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
import random

randlist = []
randlist_new = []

i = 0 # Задается произвольный список из целых чисел длинной от 20 до 50 элементов
while i < random.randrange(20,50):
    randlist.append(random.randrange(1,100))
    i += 1

print(randlist, 'Начальный список \n')

for r in randlist:
    if (r % 2) == 0:
        randlist_new.append(r / 4)
    else:
        randlist_new.append(r * 2)

print(randlist_new, 'Итоговый список')