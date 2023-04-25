
from Hometask1_lesson5.utils import calculate_change

price = input("Введите стоимость товара: ")
paid = input("Введите купюры внесенные в кассу: ")

change = calculate_change(price, paid)

print(f'Купюры для сдачи: {change}')


