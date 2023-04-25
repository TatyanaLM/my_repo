from collections import Counter
import random
lst = ['apple', 'peach', 'banana', 'peach', 'strawberry', 'banana', 'apple']

print(Counter(lst))

#бросить кубик тысячу раз и посчитать каунтером сколько каких значений выпало

lst = []
for i in range(1000):
    lst.append(random.randint(1, 6))
print(Counter(lst))

lst = []
x = 1000
while x != 0:
    lst.append(random.randint(1, 6))
    x -= 1
print(Counter(lst))

x = 1000
lst = [random.randint(1, 6) for i in range(x)]
print(Counter(lst))