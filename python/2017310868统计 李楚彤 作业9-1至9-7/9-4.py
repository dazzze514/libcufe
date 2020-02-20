#9-4就餐人数
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0

    def describe_restaurant(self):
        """打印信息"""
        print("The restaurant name is "+self.restaurant_name+'.')
        print("The cuisine type in the restaurant is "+self.cuisine_type+'.')

    def open_restaurant(self):
        """指出餐馆正在营业"""
        print(self.restaurant_name+" is open.")

    def number(self):
        print(str(self.number_served)+" people have enjoyed a meal at "+self.restaurant_name)

    def set_number_served(self,num):
        self.number_served=num

    def read_number_served(self):
        print(str(self.number_served))

    def increment_number_served(self,nums):
        self.number_served +=nums


restaurant_0=Restaurant('Chinese Style','chinese cuisine')
restaurant_0.number()

restaurant_0.number_served=3
restaurant_0.number()

restaurant_0.set_number_served(6)
restaurant_0.read_number_served()

restaurant_0.increment_number_served(10)

