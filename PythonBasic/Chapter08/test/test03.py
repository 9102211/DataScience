#3.파일 life.txt가 있다. 이 파일의 내용 중 "java"라는 문자열을 "python"으로 바꾸어서 저장해 보자.

try:
    read = open("file/life.txt", mode="r")
    str = read.read().replace('java', 'python')
    read.close()

    edit = open("file/life.txt", mode="w", encoding="utf-8")
    edit.write(str)
    edit.close()

except Exception as e:
    print("error 발생 : ", e)