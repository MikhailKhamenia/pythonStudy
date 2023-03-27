favorite_numbers = [6, 57, 4, 7, 68, 95]
my_iterator = iter(favorite_numbers)

print(next(my_iterator))
print(next(my_iterator))


class Count:
    """Итератор, который считает до бесконечности."""

    def __init__(self, start=0):
        self.num = start

    def __iter__(self):
        return self

    def __next__(self):
        num = self.num
        self.num += 1
        return num

for n in Count():
    print(n)