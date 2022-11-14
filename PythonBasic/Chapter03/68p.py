import random

names = ['김레드','오렌지','명노랑','한그린','나하늘','이블루','최보라','연분홍','김블랙']
print(names)
print(names[2])

if '이블루' in names:
    print('이블루 있음')
else:
    print('이블루 없음')

idx = random.randint(0,8)
print(f'{names[idx]} 바보')