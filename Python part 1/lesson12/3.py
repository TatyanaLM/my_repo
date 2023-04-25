def return_fun(n):
    for k in range(0, n):
        return k

print(return_fun(10))

#next()
#yield

def generator(n):
    for y in range(0, n):
        yield y

return_res = return_fun(55)
my_range = generator(10)

print(list(my_range))

for i in generator(10):
    print(i)

new_range = generator(2)
print(next(new_range))
print(next(new_range))

#__iter__
#__next__

class Generator:
    counter = 0

    def __init__(self, number):
        self.number = number

    def __next__(self):
        if self.counter < self.number:
            result = self.counter
            self.counter += 1
            return result
        else:
            return StopIteration()

    def __iter__(self):
        return self

new = Generator(5)
print(list(new))