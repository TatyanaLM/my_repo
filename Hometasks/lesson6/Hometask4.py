# Используя random.sample сгенерируйте список случайных элементов.
# Используйте List comprehension.

import random

elem = ['red', 523, 'jfgfg', 'Мира', 'Кирилл', '34', 734, 900]
random_elem = [random.sample(elem, 3, counts=None) for i in range(4)]
print(random_elem)
