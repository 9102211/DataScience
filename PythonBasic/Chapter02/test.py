#문제1
print("문제1")
kor=80
eng=75
math=90
sci=95
average=((kor+eng+math+sci)/4)
print("평균 :", average)

#문제2
print("문제2")
num1 = 13
print(num1%2)
num2 = 16
print(num2%2)

#문제3
print("문제3")
jumin= "881120-1068234"
print(jumin.index("-")) #참고
print(jumin[:6])
print(jumin[7:])

#문제4
print("문제4")
print(jumin[7])

#문제5 a#b#c#d로 바꿔 출력
print("문제5")
str="a:b:c:d"
str = str.replace(":", "#")
print(str)

#문제6
print("문제6")
list = ['\"우리', '끝까지', '힘내요!\"']
print(' '.join(list))

