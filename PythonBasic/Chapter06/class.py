class calc_class:
    x = y = 0

    def __init__(self, a, b):
        self.x = a
        self.y = b

    def plus(self):
        p = self.x + self.y
        return p

    def minus(self):
        m = self.x - self.y
        return m

obj = calc_class(10, 20)

print(f'plus = {obj.plus()}')
print(f'minus = {obj.minus()}')