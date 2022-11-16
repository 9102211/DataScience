#q4. 세 개의 숫자를 입력받아 가장 큰수를 출력하는 print_max 함수를 정의하라. 단 if 문을 사용해서 수를 비교하라.

def print_max(n1, n2, n3):
    max = 0
    if(n1 > n2):
        if(n1 > n3):
            max = n1
        else:
            max = n3
    else:
        if(n2 > n3):
            max = n2
        else:
            max = n3
    print(f"max= {max}")

n1 = int(input('숫자를 입력해주세요 : '))
n2 = int(input('숫자를 입력해주세요 : '))
n3 = int(input('숫자를 입력해주세요 : '))

print_max(n1, n2, n3)