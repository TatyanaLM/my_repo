"""Задача: Написать программу, которая использует глобальную переменную x и локальную переменную y.
Присвоить переменной x значение 10, а переменной y - значение 5.
 Затем внутри функции изменить значение x на x*y и вернуть его.
 Вывести результат на экран."""


x = 10

def multiply_x_by_y(x):
    y = 5
    x = x * y
    return x

result = multiply_x_by_y(x)
print(result)


assert multiply_x_by_y(x) == 50