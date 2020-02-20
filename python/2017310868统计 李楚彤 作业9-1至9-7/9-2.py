#9-2创建餐馆的实例
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
        print(self.restaurant_name.title+" is open.")

restaurant_1=Restaurant("Pizza's","West")
restaurant_2=Restaurant("Chinese",'Chinese')
restaurant_3=Restaurant("Banfan",'Korean')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
