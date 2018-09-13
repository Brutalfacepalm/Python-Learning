# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000
# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.

names = ['Ivan', 'Andrey', 'Olga', 'Vladimir', 'Petr', 'Ekaterina', 'Elena', 'Alexey', 'Dmitry', 'Marina', 'Aleksandr',
         'Natalia', 'Svetlana', 'Sergey']
salarys = [35466, 68433, 89763, 12335, 665486, 18963, 45623, 46378, 96431, 76531, 563442, 411654, 345694, 65432]

bukh = dict(zip(names, salarys)) # zip для объединения двух списков, dict для преобразования в словарь
with open('salary.txt', 'w', encoding='utf-8') as file: # перезапись в файл(не совсем понял как работает(ли) w+ и r+)
    for n, s in bukh.items(): # выдергиваем поочередено ключ и значение
        file.write('{} - {}\n'.format(n, s)) # записываем ключ и значение в файл
with open('salary.txt', 'r', encoding='utf-8') as file:# чтение из файла
    for person in file: # читаем построчно (str)
        n, s = person.split()[0].upper(), round(int(person.split()[2]) * 0.87, 2)# разбиваем на переменные
        if s < 500000:
            print('{} - {}'.format(n, s))