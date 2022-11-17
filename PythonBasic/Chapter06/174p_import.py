import datetime
from datetime import date, time

########################date클래스
#help(date)

today = date(2022, 11, 17)
print(today)

#date 객체 맴버변수 호출
print(today.year)
print(today.month)
print(today.day)

#date 객체 메서드 호출
w=today.weekday()
print('요일 정보 : ', w)
print()

#######################time클래스
#help(time)

currTime = time(21, 4,30)
print(currTime)

#time 객체 멤버변수 호출
print(currTime.hour)
print(currTime.minute)
print(currTime.second)

#time 객체 메서드 호출
isoTime = currTime.isoformat()
print(isoTime)
