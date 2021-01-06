#parent class
class User:
    name = "Leia"
    email = "lOrgana@gmail.com"
    password = "qwer123"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The password or email is incorrect.")

#child class
class Rebel(User):
    department = "General"
    pin_num = "7579"

#same method in parent class "User,
#instead of using entry_password, we're using "pin_num"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_pin = input("Enter your pin: ")
        if (entry_email == self.email and entry_pin = self.pin_num):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The pin or email in incorrect.")

#second child class
class Pilots(User):
    department = "Fighters"
    pin_num = "0236"

#same method in parent class "User,
#instead of using entry_password, we're using "pin_num"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_planeNum = input("Enter your aircrafts number: ")
        if (entry_email == self.email and entry_planeNum = self.entry_planeNum):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The pin or email in incorrect.")

#polymorphism?

Jedi = User()
Jedi.getLoginInfo()

pilot = Pilots()
Pilots.getLoginInfor

manager = Rebel()
manager.getLoginInfo
