#User
class User():
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
    def describe_user(self):
        print("The user's name is "+self.first_name.title()+" "+self.last_name.title())
        print("The user is "+str(self.age)+" years old.")

    def greet_user(self):
        print("Hello,"+self.first_name.title()+" "+self.last_name.title())

user_1=User('Amy','Green',17)
user_2=User('Bob','Hawkin',18)

user_1.describe_user()
user_1.greet_user()
user_2.describe_user()
user_2.greet_user()




        

    
