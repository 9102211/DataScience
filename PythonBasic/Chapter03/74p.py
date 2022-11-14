#python 구구단
#구구단 출력 : range()함수 사용

for i in range(2, 10):
    print('--- {}단 ---'.format(i))

    #inner for
    for j in range(1, 10):
        print('%d * %d = %d'%(i, j, i*j))
