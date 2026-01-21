#                           CLI PASSWORD MANAGER

import json
import os

File = "passwords.json"

if not os.path.exists(File):
    with open(File, "w") as f:
        json.dump({}, f)

with open(File, "r") as f:
    data = json.load(f)


while True:
    p = input("Do you want to add, view, delete or change password ?\n 1.yes 2.no\n")

    if p.lower() == "yes":
        choice = input("Enter your choice:\n1.add password\n2.view password\n3.delete password\n4.change password\n5.Back\n")

        if choice.lower() == "add password":
            website = input("Enter website/app name :").lower()

            username = input("Enter username or I'd : ").lower()

            password = input("Enter password : ")
        #after taking input of the passsword the website name, username or I'd and password will get stored in the json file.

            if website == "" or username == "" or password == "":
                print("Input cannot be empty.")
                continue
            #the above loop is used as if the user provides empty input then no data will be saved. to avoid this we have used this
        
            if website in data:
                print("Website already exists. Choose change password" )
                
            data[website] = {"username": username,
                         "password": password}
        #adding the format of given as input to the program and differentiating info about username and password according to the name of website

            with open(File, "w") as f:
                json.dump(data, f) #pasting the data given in python to json file

            print("Password Saved!")
        


        elif choice.lower() == "view password":

            website = input("Enter website :").lower() #this input is to be given to make the computer known of which website do you want to access the username and password of as the password manager stores the username along with the password of different websites of the user.
            #moreover in every different elif the particular variable website acts as a new variable from which you are taking input from

            if website in data :  #checks if the website you want to view the password along with the username exists in json file or not
                print("Your Username :", data[website]["username"])
                print("Your password :", data[website]["password"])

            else:
                print("Website not found")

        elif choice.lower() == "delete password":
            website = input("Enter website : ").lower()

            if website in data : #checks if the website you want to delete exists in json file or not 
                del data[website]

            else:
                print("Website not found")

            with open(File,"w") as f:
                json.dump(data, f) #by doing this we have deleted the data[website] i.e. the data of the particular website present in json file we want to delete data of  

            print("Password Deleted Successfully")


            

        elif choice.lower() == "change password":

            website = input("Enter website :").lower()

            if website in data :
                new_password = input("Enter new password :")

                data[website]["password"] = new_password  #This data[website]["password"] at first was equal to password variable now I am making it equal to new password in the given if loop of change password
                with open(File, "w") as f:
                    json.dump(data, f)
                
                print("Password changed successfully")

            else:
                print("Website not found")



        elif choice.lower() == "back":
            continue # by this if i have chosen wrong choice then i can go back and then can select another choice.

        else:
            print("Invalid Input. Input correct choice from the choices given")
            continue



    elif p.lower() == "no":
        exit()

    else:
        print("Invalid Input")
