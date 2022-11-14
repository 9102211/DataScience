#마름모 출력 프로그램
#밑변의 길이를 입력받아 출력


while True:
    num = int(input('홀수를 입력하세요(0<-종료): '))

    if not num:
        print("마음모 프로그램 출력을 이용해 주셔서 감사합니다.")

    mid = int(input(num/2) +1 )

    for i in range(0,mid):
        for j in range(0, mid):
            print("*", end='')
        print("")