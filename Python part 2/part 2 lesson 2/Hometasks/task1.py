"""Задача: Написать программу, которая принимает на вход два числа и выводит на экран результат их умножения.
При этом использовать только базовые операции сложения, вычитания и условных операторов."""

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
def multiply(a,b):
    return a * b


print("Результат умножения:", multiply(a, b))


assert multiply(2, 3) == 6
assert multiply(10, 5) == 50
assert multiply(7, -3) == -21