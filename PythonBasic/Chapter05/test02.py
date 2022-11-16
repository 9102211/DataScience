#q2.입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자. (단 입력으로 들어오는 수의 개수는 정해져 있지 않다.)

dataset = []
def avg(data):

    dataset.append(data)

    total = 0
    for i in range(len(dataset)):
        total = total + dataset[i]

    average = total/len(dataset)

    print(f'입력값 : {dataset}\n  평균 : {round(average,1)}\n')

while True:
    avg(int(input("수 입력 : ")))