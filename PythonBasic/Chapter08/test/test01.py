#1.	다음은 "test.txt"라는 파일에 "Life is too short" 문자열을 저장한 후 다시 그 파일을 읽어서 출력하는 프로그램이다.

import os
print("D:/Pywork/DataScience/PythonBasic/Chapter08", os.getcwd())

try:
    wtest = open("file/test.txt", mode="w")
    wtest.write("Life is too short")
    wtest.close()

    rtest = open("file/test.txt", mode="r")
    print(rtest.read())
    rtest.close()

except Exception as e:
    print("error 발생 : ", e)



