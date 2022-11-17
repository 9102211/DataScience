#5.	<연습생 아이돌 만들기> '연습생.txt' 파일의 이름을 읽어와 리스트로 만든다.

def show_candidates(candidate_list):
    print(candidate_list)

def make_idol(candidate_list):
    for name in candidate_list:
        print(f'신예 아이돌 {name} 인기 급상승')

def make_world_star(candidate_list):
    for name in candidate_list:
        print(f'아이돌 {name} 월드스타 등극')


candidates_list=[]

file = open("file/연습생.txt", mode="r", encoding="utf-8")
names = file.readlines()
for name in names:
    candidates_list.append(name.strip())

show_candidates(candidates_list)
make_idol(candidates_list)
make_world_star(candidates_list)