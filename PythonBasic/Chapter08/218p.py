import os
print("D:/Pywork/DataScience/PythonBasic/Chapter08", os.getcwd())

try:
    ftest = open("data/ftest.txt", mode= "r")
    print(ftest.read())

    ftest2 = open("data/ftest2.txt", mode= "w")
    ftest2.write("my first text !!")

    ftest3 = open("data/ftest3.txt", mode= "a")
    ftest3.write("\nmy second text !!")

except Exception as e:
    print("error 발생 : ", e)

finally:
    ftest.close()
    ftest2.close()
    ftest3.close()