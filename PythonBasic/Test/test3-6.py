"""나이를 입력 받아 나이에 따른 더조은 IT공원 입장료를 계산 하는 프로그램을 작성하시오.

0~3세:무료
4~13세: 2000원
14~18세: 3000원
19~65세: 5000원
66세 이상: 무료

[화면 출력]
나이를 입력하세요.
요금은 []원 입니다. (무료인 경우 "요금은 무료입니다.")"""

age = int(input('나이를 입력하세요: '))
price = ''

if (age>=4) and (age<=13):
   price = '2000원'
elif (age>=14) and (age<=18):
    price = '3000원'
elif (age>=19) and (age<=65):
    price = '5000원'
elif (age>=0) and (age<=3):
    price = '무료'
elif (age>=66):
    price = '무료'
else:
    price = 'N/A'

print(f'요금은 {price}입니다')