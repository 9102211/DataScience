#문제9. 공원 요금 계산 프로그램 ver4

age = int(input('나이를 입력하세요: '))
price = 0
grade = ''
if (age>=0) and (age<=3):
    grade = '유아'
    print(f'귀하는 [{grade}]등급이며, 요금은 [무료]입니다')
    quit()
elif (age>=4) and (age<=13):
   price = 2000
   grade = '어린이'
elif (age>=14) and (age<=18):
    price = 3000
    grade = '청소년'
elif (19<=age<=65):
    price = 5000
    grade = '성인'
elif (age>=66):
    grade = '노인'
    print(f'귀하는 [{grade}]등급이며, 요금은 [무료]입니다')
    quit()
else:
    print('다시 입력하세요')
    quit()

print(f'귀하는 [{grade}]등급이며, 요금은 [{price}]원 입니다')

#입장료 계산
type = int(input('요금 유형을 선택하세요. (1: 현금, 2: 공원 전용 신용 카드)>>'))

if(type == 1):
    print('1.현금 결제')
    payment = int(input('요금을 입력하세요: '))

    if (price>payment):
        print(f'[{price-payment}]원이 모자랍니다. 입력하신 [{payment}]원을 반환합니다')
    elif (price==payment):
        print('감사합니다. 티켓을 발행합니다')
    elif (price<payment):
        print(f'감사합니다. 티켓을 발행하고 거스름돈 [{payment-price}]원을 반환합니다.')

elif(type == 2):
    print('2.카드 결제')
    if(age >=60 and age<=65):
        discount = price * 0.85
        print(f'[{discount}]원 결제 되었습니다. 티켓을 발행합니다')
    else:
        discount = price * 0.9
        print(f'[{discount}]원 결제 되었습니다. 티켓을 발행합니다')
else:
    print('다시 입력해 주세요')
    quit()