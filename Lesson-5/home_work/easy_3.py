# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import os
import sys
import shutil


def copy(name):
    shutil.copy(name, name + '.bak')

if __name__ == '__main__':
    name = os.path.basename(sys.argv[0])
    copy(name)