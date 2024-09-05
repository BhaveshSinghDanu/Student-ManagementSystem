import home
class Login:
    def __init__(self,name,pwd):
        self.name=name
        self.pwd=pwd
    def checkCreds(self):
        if self.name=='admin' and self.pwd=='1234':
            return True
        else:
            return False


def signin():
    name=input('enter user name:')
    pwd=input('enter user pwd:')
    obj=Login(name,pwd)
    if obj.checkCreds():
        home.homescreen()
    else:
        print("Try again!")
        signin()

signin()