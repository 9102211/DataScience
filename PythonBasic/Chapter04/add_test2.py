#문제2.(1,2,3)이라는 튜플에 4라는 값을 추가하여 (1,2,3,4)처럼 만들어 출력해 보자

tuple1 = (1,2,3)

tuple1 += (4,)

print(tuple1)



"""
굳이변환안해도된다~~

lst = list(tuple1)
lst.append(4)

tuple1 = tuple(lst)
"""