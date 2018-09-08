# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y

equation = equation.split()
b = float(equation.pop(-1))
k = float(equation.pop(-2)[:-1:])

y = k * x + b

print('Координатa точки по оси y = {}'.format(y))