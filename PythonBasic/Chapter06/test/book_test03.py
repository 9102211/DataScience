class Person:
    def __init__(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age

    def display(self):
        print("=" * 30)
        print(f"이름:{self.name}, 성별:{self.gender}\n나이:{self.age}")
        print("=" * 30)

##############################################
name = input("이름 입력 : ")
age = input("나이 입력 : ")
gender = input("성별 입력 : ")

p = Person(age, name, gender)
p.display()