
"""Задача: Написать программу, которая вычисляет значение математического выражения, заданного строкой.
Строка содержит только цифры и операторы сложения, вычитания, умножения и деления.
При этом использовать только базовые операции и функции."""

def calculate(str):
    list_str = list(str)
    new_list = []
    for current in list_str:
        if current == "+" or current == "-" or current == "/" or current == "*":
            new_list.append(current)
        else:
            new_list.append(int(current))
    print(new_list)
    for i in range(len(new_list)):
        if new_list[i] == "*" or new_list[i] == "/":
            if new_list[i] == "*":
                num = new_list[i-1] * new_list[i+1]
                new_list[i-1] = num
                new_list[i+1] = "none"
            else:
                num = new_list[i-1] / new_list[i+1]
                new_list[i-1] = float(num)
                new_list[i+1] = "none"
    print(new_list)
    result = 0
    for i in range(len(new_list)):
        if new_list[i] == "+":
            result = result + new_list[i-1] + new_list[i+1]
        elif new_list[i] == "-":
            result = result + new_list[i-1] - new_list[i+1]
        else:
            pass
    return result


assert calculate("2+3*4-5/2") == 10.5
assert calculate("1+2+3+4+5") == 15
assert calculate("10*5-7*3+2") == 23
