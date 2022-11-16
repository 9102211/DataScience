#레스토랑 클래스 만들기
class Restaurant:
    restaurant_name = cuisine_type = ""
    def __init__(self,name,type):
        self.restaurant_name = name
        self.cuisine_type = type

    def describe_restaurant(self):
        print(f"저희 레스토랑 명칭은 [{self.restaurant_name}] 이고 [{self.cuisine_type}] 전문점입니다.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} 레스토랑 OPEN !!!\n")

    def __del__(self):
        print(f"{self.restaurant_name} 레스토랑 문닫아용")

res_list = []
for i in range(3):
    name,type = input("레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분) : ").split()
    res_list.append(Restaurant(name,type))
    res_list[i].describe_restaurant()
    res_list[i].open_restaurant()

print("""
 .
 .
시간이 지나 밤이 되었습니다
 .
 .
""")