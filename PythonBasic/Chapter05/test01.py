#q1. 주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해 보자.

def is_odd(num):
    if num % 2 == 0:
        print(f'{num} : 짝수')
    elif num % 2 == 1:
        print(f'{num} : 홀수')

is_odd(int(input("자연수를 입력하세요 >> ")))