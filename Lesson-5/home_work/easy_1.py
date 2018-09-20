# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os

def create(name):
    if not name in os.listdir():
        os.mkdir(name) # создание директорий dir_1 - dir_9


def delete(name):
    if name in os.listdir():
        os.rmdir(name)  # удаление директорий dir_1 - dir_9, если они существуют



if __name__ == '__main__':
    for i in range(1, 10):
        name = 'dir_' + str(i)
        create(name)
        # delete(name)

