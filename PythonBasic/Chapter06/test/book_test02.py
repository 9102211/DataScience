from math import sqrt
from statistics import mean

x = [5, 9, 1, 7, 4, 6]

class Scattering:
    def __init__(self, x):
        self.x = x

    def var_func(self):
        avg = mean(self.x)
        diff = [(i-avg) ** 2 for i in self.x]

        self.var = sum(diff) / (len(self.x) - 1 )
        return print(f"분산 : {self.var}")

    def std_func(self):
        st = sqrt(self.var)
        return print(f"표준편차 : {st}")


p = Scattering(x)
v = p.var_func()
s = p.std_func()
