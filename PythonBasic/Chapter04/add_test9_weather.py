#문제9. 표의 데이터를 딕셔너리에 저장한 다음 출력하는 프로그램을 작성하시오.
import math

weather = {'월':25.5, '화':28.3, '수':33.2, '목':32.1, '금':17.3, '토':35.3, '일':33.3}

for key in weather.keys():
    print(f"{key}", end="\t\t")

print("\n-----------------------------------------------------")
for key in weather.keys():i
    print(f"{weather[key]}˚",end="\t")


#문제10. 최저기온
print(f"\n\n최저기온: {min(weather.values())}˚\n")

#문제11. 30도 이상인 날
weather_hot = []
for key in weather.keys():
    if weather[key] >= 30.0:
        weather_hot.append(key)

print(f"기온이 30˚ 이상인 요일 : {weather_hot}\n")


#문제12.	딕셔너리에서 일주일간의 평균 기온을 구하는 프로그램을 작성하시오.
avg_air = 0
for key in weather.keys():
    avg_air += weather[key]

avg_air = avg_air/7

print(f"일주일간의 평균 기온 : {round(avg_air,1)}˚\n")