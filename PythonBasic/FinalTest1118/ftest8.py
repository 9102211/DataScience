#8. 페이지 수를 출력하는 프로그램
import math

def getTotalPage(m, n):
    page = math.ceil(m / n)
    return page

print(getTotalPage(5, 10)) # 1 출력
print(getTotalPage(15, 10)) # 2 출력
print(getTotalPage(25, 10)) # 3 출력
print(getTotalPage(30, 10)) # 4 출력