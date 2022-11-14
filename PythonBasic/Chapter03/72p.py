num1 =range(10)
print(f'num1 :{num1}')
num2 = range(1,10)
print(f'num2 :{num2}')
num3 = range(1,10,2)  # range(1:start, 10:stop, 2:step)
print(f'num3 :{num3}')

#range 객체 활용
for n in num1 :
    print(n, end = ' ')
print()
for n in num2 :
    print(n, end = ' ')
print()
for n in num3 :
    print(n, end = ' ')
print()
