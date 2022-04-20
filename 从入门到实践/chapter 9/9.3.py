class User():
    def __init__(self,first_name,last_name,login_attempts):
        self.first_name=first_name
        self.last_name=last_name
        self.login_attempts=login_attempts

    def describe_user(self):
        print(self.first_name+'.'+self.last_name)

    def greet_user(self):
        print(self.first_name+'.'+self.last_name+' 你咋这么帅呢')

    def increent_login_attempts(self):
        self.login_attempts+=1
        print(self.login_attempts)

    def reset_login_attempts(self):
        self.login_attempts=0
        print(self.login_attempts)
user=User('尼古拉斯','为何王如此帅',0)

user.describe_user()
user.greet_user()
user.increent_login_attempts()
user.increent_login_attempts()
user.reset_login_attempts()

class Admin(User):
    def __init__(self,first_name,last_name,login_attempts,privileges):
        super().__init__(first_name,last_name,login_attempts)
        self.privileges=privileges

    def show_privileges(self):
        print(self.privileges)

admin=Admin('尼古拉斯','为何王如此帅',0,['eat ao li gei','diao fen'])
admin.show_privileges()



