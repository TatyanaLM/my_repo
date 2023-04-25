
lst2 = [1, 2, {}, 6, 77, 88]
def all_func(iter):
    for element in iter:
        if not element:
            return False
    return True

print(all_func(lst2))