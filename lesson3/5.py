#names = ["Romeo", "Kevin", "Eden", "Jan", "Mickey"]
#names.append([1,2,3]) добавляем еще один элемент
#print(names[-1][2])

#names = ["Romeo", "Kevin", "Eden", "Jan", "Mickey"]
#names.extend([1,2,3]) добавляем в список новые эл-ты
#print(names)

#names = ["Romeo", "Kevin", "Eden", "Jan", "Mickey"]
#names.insert(1, True) добавили эл-т в список в середине
#print(names)

#names = ["Romeo", "Kevin", "Eden", "Jan", "Mickey", "Jan"]
#names.remove("Jan") удаляем эл-т из списка
#print(names)

#names = ["Romeo", "Kevin", "Eden", "Jan", "Mickey", "Jan"]
#names.pop((0)) удаляем первый эл-т Ромео
#print(names)

#names = ["Romeo", "Kevin", "Eden", "Jan", "Mickey", "Jan"]
#print(names.index("Jan")) выводим номер эл-та Джен - первой встретившиейся

n = int(input("Введите количество элементов в списке "))
lst = []
for i in range(n):
    lst.append(input())

print(lst)