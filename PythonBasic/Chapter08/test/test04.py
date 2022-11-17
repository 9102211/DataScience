#4.인사하는 프로그램

file = open("file/python greet_user.txt", mode="r")
usernames = file.read().split()
def greet_users(usernames):
    for name in usernames:
        print(f'Hello, {name[0:].capitalize()}!')

greet_users(usernames)