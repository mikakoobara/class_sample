class Product:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
    def discount(self, price):
        self.amount -= price
        #self.amount price


if __name__ == "__main__":
    p1 = Product("iPhone", 100000) #Prductクラスのインスタンス化
    print(p1)

    print(p1.name)   #iPhone
    print(p1.amount)  #100000
    p1.discount(5000)
    print(p1.amount)  #95000

    p2 = Product("MBA", 150000)
    print(p2.name)  # MBA
    print(p2.amount)  # 150000
    p2.discount(9800)
    print(p2.amount)
