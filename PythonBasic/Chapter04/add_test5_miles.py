#문제5. 아이디와 마일리지 포인트를 딕셔너리에 저장한 다음 출력하는 프로그램을 작성하시오.

miles = {'kim99': 12000, 'lee66': 11000, 'han55': 3000, 'hong77': 5000, 'hwang33': 18000}

print("문제5")
for key in miles.keys():
    print(f"아이디: {key}, 마일리지: {miles[key]}")


#문제6.	아이디 'han55'의 마일리지를 5000점으로 업데이트하고 업데이트된 정보를 출력하는 프로그램을 작성하시오.
ID = 'han55'    #참고 : 상수는 대문자로 선언

miles[ID] = miles.get(ID) + 2000

print(f"\n문제6\n {ID}님의 마일리지가 {miles[ID]}점으로 수정되었습니다.\n")


#문제7. 딕셔너리에 아이디 'jang88'과 마일리지 7000을 추가한 다음 전체 딕셔너리와 추가된 데이터를 출력하는 프로그램을 작성하시오.
miles['jang88'] = 7000

print(f"문제7\n 전체 딕셔너리 : {miles}")
print(f"jang88님의 마일리지 {miles['jang88']}점이 추가되었습니다.\n")

#문제8. 딕셔너리에서 가장 높은 마일리지를 찾아서 출력하는 프로그램을 작성하시오.
max_miles = max(miles.values())
for key in miles.keys():
    if miles[key] == max_miles:
        max_id = key

print(f"문제8\n {max_id}님의 {max_miles}점이 가장 높은 점수입니다.")