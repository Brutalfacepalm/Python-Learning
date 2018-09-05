# coding: utf-8
number = 0
while number == 0:
    number = int(input('Введи число от 0 до 10: '))
    if 0 < number < 10:
        print('Вот тебе квадрат твоего числа:', number**2)
        break
    else:
        print('Это не правильное число. Введи только от 0 до 10.')
        number = 0