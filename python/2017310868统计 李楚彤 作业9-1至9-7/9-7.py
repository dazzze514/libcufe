#9-7管理员
class User():
    def __init__(self,first_name,last_name,age,login_attempts):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.privileges=['can add post','can delete post','can ban post']

    def show_privileges(self):
        print(self.privileges)

class Admin(User):
    def __init__(self,first_name,last_name,age,login_attempts):
        super().__init__(first_name,last_name,age,login_attempts)

Admin_0=Admin('Amy','Green',16,1)
Admin_0.show_privileges()
