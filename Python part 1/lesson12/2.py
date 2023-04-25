def takeClosest(num, collection):
    return min(collection, key = lambda x:abs(x-num))

lst = [1, 2, 3, 4, 5, 6, 7, 9]
print(takeClosest(8, lst))


def takeClosest(self, diff, visa_list):
    return min(visa_list, key=lambda x: abs(x - num))


def next_visa(self):
    for i in visa_list:
# if diff