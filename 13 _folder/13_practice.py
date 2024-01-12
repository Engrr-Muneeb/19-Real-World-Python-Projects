#code:1
class product:
    quantity = 400

    def __init__(self,name,price):
        self.name = name
        self.price = price

p1 = product("T shirt","10")
print(p1.name)
print(p1.price)

#code:2
class product:

    def __init__(self,name,price):
        self.name = name
        self.price = price

    def get_data(self):
        self.name = input('Enter name of the product:\n')
        self.price = input('Enter price of the product:\n')

    def put_data(self):
        print(self.name)
        print(self.price)

p1 = product("","")
p1.get_data()
p1.put_data()