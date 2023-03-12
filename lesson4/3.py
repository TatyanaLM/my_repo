
cars = (input("Введите список машин: "))
names = (input("Введите список имен: "))

names = names.split(',')
cars = cars.split(',')

names = sorted(names)
cars = sorted(cars)

if len(cars) == len(names):
    result = list(zip(names, cars))
    print(result)

elif len(cars) != len(names):
    print("Кому-то не достанется автомобиля!")