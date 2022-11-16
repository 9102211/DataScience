#7. 문자열 하나를 입력받아 인터넷 주소를 반환하는 make_url 함수를 정의하라.make_url("naver")www.naver.com

def make_url(str):
    print(f'주소 반환: https://www.{str}.com')

make_url(str=input("사이트명 입력: "))