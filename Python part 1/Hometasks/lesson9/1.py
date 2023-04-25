
def calculate(expr):
    try:
        result = eval(expr)
        return result
    except:
        return "Ошибка в выражении."

expr = input("Введите выражение: ")
print(calculate(expr))