#문제10. 공원 요금 계산 프로그램 ver5
"""7번째 손님 마다 티켓 구매시 무료 티켓을 발행한다. (초기 무료 티켓: 3장)
4번째 손님 마다 티켓 구매시 연간 회원권 홍보 이벤트를 진행한다. (초기 할인 티켓: 5장)"""

count = 0
free_ticket = 3
discount_ticket = 5
while True:
    age = int(input('나이를 입력하세요: '))
    price = 0

    if (0 <= age <= 3):
        grade = '유아'
        price = 0
    elif (4 <= age <= 13):
       price = 2000
       grade = '어린이'
    elif (14 <= age <= 18):
        price = 3000
        grade = '청소년'
    elif (19 <= age <= 65):
        price = 5000
        grade = '성인'
    elif (age >= 66):
        grade = '노인'
        price = 0
    else:
        print('다시 입력 해 주세요')
        continue

    if(price==0):
        print(f'귀하는 [{grade}]등급이며, 요금은 무료입니다')
    else:
        count += 1
        print(f'귀하는 [{grade}]등급이며, 요금은 [{price}]원 입니다')

        #입장료 계산
        type = int(input('요금 유형을 선택하세요. (1: 현금, 2: 공원 전용 신용 카드)>>'))

        if(type == 1):
            print('1.현금 결제')
            payment = int(input('요금을 입력하세요: '))

            if (price>payment):
                print(f'[{price-payment}]원이 모자랍니다. 입력하신 [{payment}]원을 반환합니다\n')
                count -= 1
            elif (price==payment):
                print('감사합니다. 티켓을 발행합니다\n')
            elif (price<payment):
                print(f'감사합니다. 티켓을 발행하고 거스름돈 [{payment-price}]원을 반환합니다.\n')

        elif(type == 2):
            print('2.카드 결제')
            if(age >=60 and age<=65):
                discount = price * 0.85    #참고 : 굳이필요없고 price에 할인해서 출력해도됨
                print(f'[{int(discount)}]원 결제 되었습니다. 티켓을 발행합니다\n')
            else:
                discount = price * 0.9
                print(f'[{int(discount)}]원 결제 되었습니다. 티켓을 발행합니다\n')
        else:
            print('다시 입력해 주세요')
            continue

        #티켓
        if (count%7==0 and free_ticket>0):
            free_ticket -= 1
            print(f"축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 무료티켓 [{free_ticket}]장\n")

        if (count%4==0 and discount_ticket>0):
            discount_ticket -= 1
            print(f"축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다."
                  f"연간 회원 할인 티켓을 발행합니다. 잔여 할인티켓 [{discount_ticket}]장\n")