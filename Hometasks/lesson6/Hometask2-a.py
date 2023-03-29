#2. Напишите программу принимающую на вход список [1,2,3] и выводящую все возможные комбинации его членов.:
#Ответ: (1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)


numbers = [1, 2, 3]
#result = []
#r = ""
for i in numbers:
    for j in numbers:
        if i != j:
            for l in numbers:
                if l != i and l != j:
                    #r = r + "(" + str(i) + ", " + str(j) + ", " + str(l) + ")" + ", "
                    print((i, j, l), end=" ")
#print(r)