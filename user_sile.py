class User:
    def __init__(self,name, age, country):
        # インスタンス変数
        self.name = name
        self.age = age
        self.country = country


    def display_profile(self):
        #diplay_profile()はUserくらすのインスタンスメソッド
        print(f"{self.name} 国籍: {self.country} 年齢:{self.age}歳")

    def change_nathionality(self,coutry_name):
         self.country = coutry_name


if __name__ == "__main__":
    bob = User("Bob", 15, "USA")   #Userクラスのインスタンス化
    bob.display_profile()
    bob.change_nathionality("China")
    bob.display_profile()


    #print(bob.name)

    tom = User("Tom", 57, "USA")
    tom.display_profile()
    tom.change_nathionality("China")
    tom.display_profile()



    ken = User("Ken", 49, "JP")
    ken.display_profile()
    ken.change_nathionality("UK")
    ken.display_profile()
