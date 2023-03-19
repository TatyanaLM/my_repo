#2. Напишите программу принимающую на вход список [1,2,3] и выводящую все возможные комбинации его членов.:
#Ответ: (1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)

def combinator(list):
    result = []
    result.append((list[0], list[1], list[2]))
    result.append((list[0], list[2], list[1]))
    result.append((list[1], list[0], list[2]))
    result.append((list[1], list[2], list[0]))
    result.append((list[2], list[0], list[1]))
    result.append((list[2], list[1], list[0]))
    return result

lst = [5, 6, 7]
print(combinator(lst))
