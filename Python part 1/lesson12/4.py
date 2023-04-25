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
print(next(new))
print(next(new))
print(next(new))