class Super:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print(f'name : {self.name}, age: {self.age}')

sup = Super('부모', 55)
sup.display() #부모 멤버 호출

class Sub(Super):
    gender = None

    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        print(f'name : {self.name}, age : {self.age}, gender : {self.gender}')

sub = Sub('자식', 25, '여자')
sub.display() #자식 멤버 호출

#Console
#name : 부모, age: 55
#name : 자식, age : 25, gender : 여자