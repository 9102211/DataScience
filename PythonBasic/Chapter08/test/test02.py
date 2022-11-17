#2.	사용자의 입력을 파일(test2.txt)에 저장하는 프로그램을 작성해 보자.

while True:
    edit = open("file/test2.txt", mode="a")
    user_input = input("저장할 내용을 입력하세요 (종료는 엔터): ")

    if user_input == '':
        break

    edit.write(user_input)
    edit.close()

