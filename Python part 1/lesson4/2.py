import itertools
from itertools import zip_longest
#result_list = list(zip_longest([1], 'abcd', (9,8,7), fillvalue=None))

a = list(range(5))
b = list(range(3,10))
result_list = list(zip_longest(a, b, fillvalue=0))
print(result_list)