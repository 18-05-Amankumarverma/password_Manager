# 1. first authenticate User then show his password
# 2. add password ask for website name and email id and password and also userid for that website
# 3. update password
# 4. delete password

import json

db = []

# custom error class
class FileNotContainDataError(FileNotFoundError):
    pass 


# load data into db varibales in list form
def load_data():
    try:
        with open("auth.txt",'r') as fs:
            try:
                loaded_data = json.loads(fs.read())
                return loaded_data
            except Exception as e:
                print(e)
    except FileNotContainDataError:
        print("File does not contain any Data")

    finally:
        fs.close()


db = load_data() # load data function called

def save_data_into_file(db):
    try:
        with open("auth.txt",'w') as fs:
            json.dump(db,fs)
    except FileNotFoundError:
        print("File not exits")
    finally:
        fs.close()


def create_account(username,password):
    if(type(username) is str) or (type(password) is str):
       if(len(username) != 0) or (len(password) != 0):
           db.append({"username":username,"password":password})
           save_data_into_file(db)
      


def login(username,password):
    if(type(username) is str) or (type(password) is str):
        if(len(username) != 0) or (len(password) != 0):
            for i in db:
                if(i["username"] == username) and (i["password"] == password):
                    return "Login Successfully"
                
    return "Login Failed"

def take_input():
    username = input("Enter your Username : ")
    password = input("Enter your Password : ")

    return username,password


def test():

    print("\n")    
    print("*"*100)
    message = "\U0001F1EE Welcome To CLI Based Password Manager \U0001F64F"
    x = message.center(100)
    print(x)
    print("*"*100)


    message = "Instructions To Use It"
    x = message.center(20)
    print('\n')
    print(x)
    print("*"*30)


    while True:
        print("1.Create Account \U0001F464 \n2.Login Into Existing Account \n3.LogOut ")
        choice = int(input("\nEnter your Command Key : "))
        match choice:
            case 1:
                message = "Create Account"
                x = message.center(50)
                print(x)
                print("*"*50)
                username,password = take_input()
                create_account(username,password)
            case 2:
                message = "Login Into Existing Account"
                x = message.center(80)
                print(x)
                print("*"*80)
                username,password = take_input()
                status = login(username,password)
                print(status)
            case 3:
                print("You Want to LogOut ! Y/N")
                LogOut_choice= str(input())
                match LogOut_choice:
                    case 'Y':
                        print("LogOut Successfully \U0001F622")
                        return
                    case 'N':
                        print("We are Happy to See you again \U0001F60A")
            case _:
                return 
            



test()