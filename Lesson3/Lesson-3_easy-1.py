# Постарайтесь использовать то, что мы прошли на уроке при решении этого ДЗ,
# вспомните про zip(), map(), lambda, посмотрите где лучше с ними, а где они излишни!

# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"
def person_info (name, age, city):
    return ('{}, {} год(а), проживает в городе {}.'.format(name.title(), age , city.title()))

print(person_info(input('Как тебя зовут? '),
                  input('Сколько тебе лет? '),
                  input('В каком городе ты живешь? ')))