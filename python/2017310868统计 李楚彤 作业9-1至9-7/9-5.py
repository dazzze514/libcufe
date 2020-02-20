#9-5尝试登录次数
class User():
    def __init__(self,first_name,last_name,age,login_attempts):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.login_attempts=login_attempts

    def increment_login_attempts(self):
        self.login_attempts +=1
        print(str(self.login_attempts))

    def reset_login_attempts(self):
        self.login_attempts=0
        print(str(self.login_attempts))
user=User('Amy','Green',16,3)
user.increment_login_attempts()

user.increment_login_attempts()

user.increment_login_attempts()

user.increment_login_attempts()

user.reset_login_attempts()

