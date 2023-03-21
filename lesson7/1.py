n = int(input("Введите число: "))

list = []
for i in range(1, n + 1):
    #print(i)
    for j in range(1, i + 1):
        list.append(i)
        #print(list)
list_result = []
for x in range(n):
    list_result.append(list[x])

#print(list)
print(list_result)
