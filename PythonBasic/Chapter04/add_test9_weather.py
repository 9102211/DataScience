#문제9. 표의 데이터를 딕셔너리에 저장한 다음 출력하는 프로그램을 작성하시오.
import math

weather = {'월':25.5, '화':28.3, '수':33.2, '목':32.1, '금':17.3, '토':35.3, '일':33.3}


LINE_NUM = 54
print('-' * LINE_NUM)   #참고~~~!

for day in weather:
    print(f"{day}", end="\t\t")

print()
print('-' * LINE_NUM)

for temp in weather:
    print(f"{weather[temp]}˚",end="\t")

print()
print('-' * LINE_NUM)

#문제10. 최저기온
print(f"\n최저기온: {min(weather.values())}˚\n")

#문제11. 30도 이상인 날
weather_hot = []
for temp in weather:
    if weather[temp] >= 30.0:
        weather_hot.append(temp)

print(f"기온이 30˚ 이상인 요일 : {weather_hot}\n")


#문제12.	딕셔너리에서 일주일간의 평균 기온을 구하는 프로그램을 작성하시오.
avg_air = 0
for temp in weather:
    avg_air += weather[temp]

avg_air = avg_air/len(weather) # = 7

#print(f"일주일간의 평균 기온 : {round(avg_air,1)}˚\n")
print("일주일간의 평균 기온 : %.1f˚" % avg_air)
