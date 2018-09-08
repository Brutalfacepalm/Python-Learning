# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]
import random

randlist, randlist_a, randlist_b = [],[],[]
i = 0
while i < random.randint(10,50):
    randlist.append(random.randint(0,20))
    i += 1

print(randlist, ' - исходны список')

for rand in randlist: # Решение задачи б
    if randlist.count(rand) == 1:
        randlist_b.append(rand)
    else:
        pass

randlist_a = list(set(randlist)) # Решение задачи а
randlist_b.sort()

print(randlist_a, ' - задача а')
print(randlist_b, ' - задача б')