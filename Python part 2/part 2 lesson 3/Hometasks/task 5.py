"""Задача 5: Допустим, у нас есть два списка одинаковой длины, names и ages,
содержащие соответственно имена и возрасты людей.
Мы хотим создать новый список строк, в которых будут указаны имена и возрасты в формате
"Имя - возраст". Напишите comprehension, который решает эту задачу
"""

names = ['Tanya', 'Vasiliy', 'Anton', 'Mark', 'Anna']
ages = [35, 67, 12, 78, 35]
sex = ['Female', 'Male', 'Male', 'Male', 'Female']

result = [f"{name} - {age} - {sex}" for name, age, sex in zip(names, ages, sex)]
print(result)
