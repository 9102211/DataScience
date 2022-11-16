class Ractangle:
    width = height = 0

    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area_calc(self):
        area = self.width * self.height
        return print(f"사각형의 넓이 : {area}")

    def circum_calc(self):
        circum = (self.width + self.height) * 2
        return print(f"사각형의 둘레 : {circum}")


########################################################
print("사각형의 넓이와 둘레를 계산합니다.")
w = int(input("사각형의 가로 입력: "))
h = int(input("사각형의 세로 입력: "))

print("-"*30)
rec = Ractangle(w,h)
area = rec.area_calc()
circum = rec.circum_calc()
print("-"*30)