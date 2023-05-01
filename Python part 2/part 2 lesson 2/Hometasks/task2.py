
"""Задача: Написать программу, которая вычисляет значение математического выражения, заданного строкой.
Строка содержит только цифры и операторы сложения, вычитания, умножения и деления.
При этом использовать только базовые операции и функции."""



def calculate(expression):
    stack = []
    num = 0
    sign = "+"
    for i, char in enumerate(expression):
        if char.isdigit():
            num = num * 10 + float(char)
        if (not char.isdigit() and not char.isspace()) or i == len(expression) - 1:
            if sign == "+":
                stack.append(num)
            elif sign == "-":
                stack.append(-num)
            elif sign == "*":
                stack.append(stack.pop() * num)
            elif sign == "/":
                stack.append(float(stack.pop() / num))
            num = 0
            sign = char
    print(stack)
    return sum(stack)

print(calculate("2+3*4-5/2"))
print(calculate("1+2+3+4+5"))
print(calculate("10*5-7*3+2"))
assert calculate("2+3*4-5/2") == 11.5
assert calculate("1+2+3+4+5") == 15
assert calculate("10*5-7*3+2") == 31


