#q1. 사칙연산 클래스 만들기

class FourCal:
    first = second = 0

    def __init__(self,first,second):
        self.first = first
        self.second = second

    def add(self):
        add = self.first + self.second
        return print(f"add : {add}")

    def sub(self):
        sub = self.first - self.second
        return print(f"sub : {sub}")

    def mul(self):
        mul = self.first * self.second
        return print(f"mul : {mul}")
    def div(self):
        div = self.first / self.second
        return print(f"div : {div}")

    def setdata(self, first, secode):
        self.first = first
        self.second = secode

first = int(input("첫번째 수 입력: "))
second = int(input("두번째 수 입력: "))

a = FourCal(first,second)
a.add()
a.sub()
a.mul()
a.div()

print("\nsetdata 호출")
first = int(input("첫번째 수 입력: "))
second = int(input("두번째 수 입력: "))
b = FourCal(3,8)
b.setdata(first, second)
b.add()
b.sub()
b.mul()
b.div()
