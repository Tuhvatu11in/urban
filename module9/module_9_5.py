class StepValueError(ValueError):
    pass

class Iterator:
    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError('шаг не может быть равен 0')
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        if (self.step > 0 and self.pointer >= self.stop) or (self.step < 0 and self.pointer <= self.stop):
            raise StopIteration
        self.pointer += self.step
        return self.pointer - self.step

# Примеры использования:

it1 = Iterator(1, 10, 2)
for i in it1:
    print(i)

it2 = Iterator(10, 1, -2)
for i in it2:
    print(i)

try:
    it3 = Iterator(1, 10, 0)
except StepValueError as e:
    print(e)

