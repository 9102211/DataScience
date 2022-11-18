#7. 10 미만의 자연수에서 3과 5의 배수를 구하면 3, 5, 6, 9이다. 이들의 총합은 23이다. 1000 미만의 자연수에서 3의 배수와 5의 배수의 총합을 구하라.

num = int(input("1000미만의 자연수 입력: "))
sum = 0
for i in range(num+1):
    if i % 3 == 0 or i % 5 == 0:
        sum += i

if 0 < num < 1000:
    print(f"총합:{sum}")
else:
    print("1000미만의 자연수를 입력하세요")
