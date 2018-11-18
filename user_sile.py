class User:
    def __init__(self,name):
        self.name = name


if __name__ == "__main__":
    user1 = User("Bob")   #Userクラスのインスタンス化

    print(user1)
    print(user1.name)

    user2 = User("Tom")
    print(user2)
    print(user2.name)

    user3 = User("Ken")
    print(user3)
    print(user3.name)
