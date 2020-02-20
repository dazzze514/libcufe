#9-1餐馆
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type

    def describe_restaurant(self):
        """打印信息"""
        print("The restaurant name is "+self.restaurant_name+'.')
        print("The cuisine type in the restaurant is "+self.cuisine_type+'.')

    def open_restaurant(self):
        """指出餐馆正在营业"""
        print(self.restaurant_name+" is open.")


my_restaurant=Restaurant('Chinese Style','chinese cuisine')
print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
