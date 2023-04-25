# Используя random.sample сгенерируйте список случайных элементов.
# Используйте List comprehension.

import random

x = 3
elem = ['red', 523, 'jfgfg', 'Мира', 'Кирилл', '34', 734, 900]
random_elem = [random.sample(elem, 3, counts=None) for i in range(x)]
print(random_elem)

random_list = random.sample([i for i in range(100)], random.randint(1, 10))
print(random_list)