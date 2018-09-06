# coding: utf-8

name = input('Как тебя зовут?\n')
age = int(input('Сколько тебе лет?\n'))
if age >= 18:
    print('Добро пожаловать, ', name + '!')
else:
    print('Тебе сюда нельзя.')
