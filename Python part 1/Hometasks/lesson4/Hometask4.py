lst = [5854, 4, 55, 718, 7, 81, 3, 659, 77, 765]
#вариант 1
def elements(lst):
    n = 0
    for i in range(1, len(lst)-1):
        if lst[i] > lst[i + 1] and lst[i] > lst[i - 1]:
            n = n + 1
        else:
            n = n
    return n
print(elements(lst))

#вариант 2
def elements2(lst):
    n = 0
    for i in range(lst):
        if lst[i] == 0:
            pass
        elif lst[i] == len(lst)-1:
            pass
        if lst[i] > lst[i + 1] and lst[i] > lst[i - 1]:
            n = n + 1
        else:
            n = n
    return n
print(elements(lst))

