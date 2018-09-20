# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import shutil
print('sys.argv = ', sys.argv)

def check_arg2():
    if not object_name:
        print("Необходимо указать второй аргумент")
        quit()
    else:
        if os.path.isabs(object_name):
            return object_name
        else:
            return os.path.join(os.getcwd(), object_name)

def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл (запросить подтверждение операции")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")

def trying(act, try_ok, try_no_ok):
    try:
        arg2 = check_arg2()
        if key == 'cp':
            act(arg2, arg2 + '.bak')
        elif key == 'rm':
            confirm = input('Если уверены, введите Y:')
            if confirm == 'Y':
                act(arg2)
            else:
                pass
        else:
            act(arg2)
        print(try_ok.format(object_name))
    except FileExistsError:
        print(try_no_ok.format(object_name))
    except FileNotFoundError:
        print(try_no_ok.format(object_name))
    except PermissionError:
        print('работать можно только с файлами')
    except NotADirectoryError:
        print('необходимо указать только папку')

def make_dir():
    trying(os.mkdir, 'директория {} создана', 'директория {} уже существует или неверно указан путь')

def ping():
    print("pong")

def copy_file():
    trying(shutil.copy, 'файл {} скопирован', 'файла {} не существует в директории')

def remove_file():
    trying(os.remove, 'файл {} удален', 'файла {} не существует в директории')

def change_dir():
    trying(os.chdir, 'директория изменена на {}', 'некорректно указан путь')

def getway():
    print(os.getcwd())

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": copy_file,
    "rm": remove_file,
    "cd": change_dir,
    "ls": getway
}

try:
    object_name = sys.argv[2]
    print(object_name)
except IndexError:
    object_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")