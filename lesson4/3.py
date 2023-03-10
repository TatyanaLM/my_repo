from itertools import zip_longest
cars = (input("Введите список машин: "))
names = (input("Введите список имен: "))

names = names.split(',')
cars = cars.split(',')

names = sorted(names)
cars = sorted(cars)
result = list(zip_longest(names, cars, fillvalue=None))

if len(cars) == len(names):
    print(result)

if len(cars) != len(names):
    print("Кому-то не достанется автомобиля!")