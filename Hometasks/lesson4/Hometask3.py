def change(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst


lst = [1, 3, 88, 15, "Karl", "7854y45", 87, "$$$$"]
print(change(lst))