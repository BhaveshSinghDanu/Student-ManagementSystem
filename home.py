import sys
import os
import json


filePresent=os.path.isfile('student.txt')


if not filePresent:
    list_name=[]
else:
    with open('student.txt','r') as f:
        st_list=f.read()
        list_name=json.loads(st_list)


def homescreen():
    print('Press the selected key')
    print('1. View Students')
    print('2. Delete Student')
    print('3. Add Student')
    print('4. exit')
    choice=input('Press key:')
    obj=Details()    
    if choice=='1':
        obj.View()
        homescreen()
    elif choice =='2':
        name=input("enter the name you want to delete:")
        obj.Delete(name)
        print(f"delete {name} successfully")
        homescreen()
    elif choice =='3':
        name=input("write name of the student you want to add: ")
        obj.Add(name)
        print(f"Added {name} successfully")
        homescreen()
    elif choice =='4':
        print("exiting")
        with open('student.txt','w') as f:
            f.write(json.dumps(list_name))
        sys.exit()
    else:
        print("wrong choice.....")
       
        homescreen()





class Details:

    def View(self):
        global list_name
        print(list_name)

    def Delete(self,name):
        global list_name
        list_name.remove(name)

    def Add(self,name):
        global list_name
        list_name.append(name)
        

