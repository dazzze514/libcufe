#9-6冰淇淋小店
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.IceCream=['strawberry ice cream','banana ice cream','milk ice cream']
    def print_ice_cream(self):
        print(self.IceCream)

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)

my_ice_cream=IceCreamStand('china','chinese')
my_ice_cream.print_ice_cream()

