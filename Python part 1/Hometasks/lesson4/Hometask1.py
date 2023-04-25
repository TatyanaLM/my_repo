def my_first_func(a, b, str):
    if str == "+":
        result = a + b
    elif str == "-":
        result =  a - b
    elif str == "/":
        result = a / b
    elif str == "*":
        result = a * b
    return result

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
x = input("Введите действие: ")
print(my_first_func(a,b,x))



