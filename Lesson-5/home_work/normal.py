# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
import easy_1
import easy_2
import easy_3
import os

def change_dir():
    name_dir = get_name_dir()
    if name_dir in os.listdir():
        os.chdir(name_dir)
        print('Теперь Вы в папке', name_dir)
    else:
        print('Папки с таким именем не существует.')

def get_name_dir():
    get_name = input('Укажите имя папки: ')
    return get_name

def move(choice):
    if choice == 1:
        change_dir()
    elif choice == 2:
        easy_2.lstdr()
    elif choice == 3:
        get_name = get_name_dir()
        if get_name in os.listdir():
            easy_1.delete(get_name)
            print('Вы удалили папку', get_name)
        else:
            print('Папки с таким именем не существует.')
    elif choice == 4:
        get_name = get_name_dir()
        if get_name not in os.listdir():
            easy_1.create(get_name)
            print('Вы создали папку', get_name)
        else:
            print('Папка с таким именем уже существует.')

choice = 0
while choice != 5:
    try:
        choice = int(input('-----------------------------------------\n'
                           '1. Перейти в папку\n'
                           '2. Просмотреть содержимое текущей папки\n'
                           '3. Удалить папку\n'
                           '4. Создать папку\n'
                           '5. Выход\n'
                           '-----------------------------------------\n'
                           'Выберите действие:\n'
                           )
                     )
        if choice == 5:
            break
        else:
            move(choice)
    except ValueError:
        print('Неверный пункт меню')

