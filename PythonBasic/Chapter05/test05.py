#5. 입력 문자열을 한 줄에 다섯글자씩 출력하는 print_5xn(string) 함수를 작성하라.

def print_5xn(string):
    start = 0
    end = len(string)

    for i in len(string)/5:
        print(string[start:end])

print_5xn(string = input("문자열 입력 : "))
