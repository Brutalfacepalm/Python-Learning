# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
import os

def lstdr():
    for i in os.listdir():
        if os.path.isdir(i):
            print(i)

if __name__ == '__main__':
    lstdr()
