#문제8. 공원 요금 계산 프로그램 ver3

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
elif (age>=19) and (age<=65):
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

payment = int(input('요금을 입력하세요: '))

if (price>payment):
    print(f'[{price-payment}]원이 모자랍니다. 입력하신 [{payment}]원을 반환합니다')
elif (price==payment):
    print('감사합니다. 티켓을 발행합니다')
elif (price<payment):
    print(f'감사합니다. 티켓을 발행하고 거스름돈 [{payment-price}]원을 반환합니다.')