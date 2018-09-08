# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)
# -*- coding: utf-8 -*-

# Предположим, что дата всегда верная.
date = '02.11.2013'

days = {u'01':'Первое','02':'Второе','03':'Третье','04':'Четвертое','05':'Пятое',
        '06':'Шестое','07':'Седьмое','08':'Восьмое','09':'Девятое','10':'Десятое',
        '11':'Одинадцатое','12':'Двенадцатое','13':'Тринадцатое',
        '14':'Четырнадцатое','15':'Пятнадцатое','16':'Шестнадцатое',
        '17':'Семнадцатое','18':'Восемнадцатое','19':'Девятнадцатое',
        '20':'Двадцатое','21':'Двадцать первое','22':'Двадцать второе',
        '23':'Двадцать третье','24':'Двадцать четвертое','25':'Двадцать пятое',
        '26':'Двадцать шестое','27':'Двадцать седьмое','28':'Двадцать восьмое',
        '29':'Двадцать девятое','30':'Тридцатое','31':'Тридцать первое'}
months = {'01':'января','02':'февраля','03':'марта','04':'апреля','05':'мая','06':'июня',
          '07':'июля','08':'августа','09':'сентября','10':'октября','11':'ноября','12':'декабря'}
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

date = date.split('.')

if int(date[2]) % 4 == 0:
    days_in_month[1] = 29
print('{} {} {} года.'.format(days.get(date[0]),months.get(date[1]),date[2]))
