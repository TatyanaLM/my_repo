def years(a):
    if a % 4 == 0 and a % 400 == 0:
        return "Год високосный"
    elif a % 4 == 0 and a % 100 != 0:
        return "Год високосный"
    else:
        return "Год невисокосный"

print(years(1600))