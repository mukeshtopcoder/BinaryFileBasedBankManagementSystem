# BANK MANAGEMENT SYSTEM
import pickle
import os
# METHOD FOR ADMIN LOGIN
def adminLogin():
    userid = "admin"
    password = "5536"
    uid = input("\n\tEnter User ID : ")
    if(uid==userid):
        pwd = input("\tEnter Password : ")
        if(pwd==password):
            adminDashboard()
        else:
            print("\tWrong Password!")
    else:
        print("\tUser Not Found!")
    input("\n\t--- Press Enter To Continue...")

# METHOD TO ADD A CUSTOMER
def addCustomer():
    file  = open("bank.dat","ab")
    ac = input("\n\tEnter A/c Number : ")
    name = input("\tEnter Customer Name : ")
    mobile = input("\tEnter Customer Phone : ")
    pwd = input("\tCreate A Password : ")
    bal = input("\tEnter Opening Balance : ")
    pickle.dump(ac,file)
    pickle.dump(name,file)
    pickle.dump(mobile,file)
    pickle.dump(pwd,file)
    pickle.dump(bal,file)
    print("\n\t--- Customer Added Successfully!")
    input("\n\n\t-- Press Enter To Continue...")
    file.close()

# METHOD TO VIEW ALL CUSTOMER
def viewAllCus():
    a = 0
    try:
        file = open("bank.dat","rb")
        while True:
            data = pickle.load(file)
            print(data,end=" ")
            a = a+1
            if(a%5==0):
                print()
    except:
        file.close()
    input("\n\tAll Customers Are Here!\n\tPress Enter To Continue...")

# METHOD TO VIEW A CUSTOMER
def viewCustomer():
    userFound = 0
    try:
        file = open("bank.dat","rb")
        uid = input("\n\tEnter A/c Number : ")
        while True:
            data = pickle.load(file)
            if(data==uid):
                print("\n\tCutomer A/c No : ",data)
                print("\tCustomer Name : ",pickle.load(file))
                print("\tCustomer Mobile : ",pickle.load(file))
                print("\tCustomer Password : ",pickle.load(file))
                print("\tCustomer Balance : ",pickle.load(file))
                userFound = 1
    except:
        file.close()
        if(userFound == 0):
            print("\n\tUser Does Not Exist!")
        input("\n\t--- Press Enter To Continue...")

# METHOD TO REMOVE/DELETE A CUSTOMER
def removeCus():
    userFound = 0
    try:
        file = open("bank.dat","rb")
        temp = open("temp.dat","ab")
        uid = input("\n\tEnter A/c Number To Delete : ")
        while True:
            data = pickle.load(file)
            if(data == uid):
                pickle.load(file)
                pickle.load(file)
                pickle.load(file)
                pickle.load(file)
                userFound = 1
            else:
                pickle.dump(data,temp)
    except:
        file.close()
        temp.close()
    os.remove("bank.dat")
    os.rename("temp.dat","bank.dat")
    if(userFound==0):
        input("\n\tCustomer Not Found!\n\tPress Enter To Continue ...")
    else:
        input("\n\tCustomer Deleted Successfully!\n\tPress Enter To Continue ...")

# METHOD FOR ADMIN DASHBOARD
def adminDashboard():
    while True:
        print("\n\n\t***** ABC BANK MANAGEMENT SYSTEM *****")
        print("\n\t1. Add Customer")
        print("\t2. Remove A Customer")
        print("\t3. Update A Customer")
        print("\t4. View All Customers")
        print("\t5. View A Customer By A/c Number")
        print("\t6. Deposit")
        print("\t7. Withdrawl")
        print("\t8. Exit")
        choice = int(input("\n\tEnter Your Choice : "))
        if(choice==8):
            print("\n\t--- Bye-Bye Admin!")
            break
        elif(choice == 1):
            addCustomer()
        elif(choice==2):
            removeCus()
        elif(choice == 4):
            viewAllCus()
        elif(choice == 5):
            viewCustomer()

# DASHBOARD
while True:
    print("\n\t***** ABC BANK MANAGEMENT SYSTEM *****")
    print("\n\t1. Admin Login")
    print("\t2. Customer Login")
    print("\t3. Exit")
    ch = int(input("\n\tEnter Your Choice : "))
    if(ch==3):
        print("\n\t--- Bye-Bye User!")
        break
    elif(ch==1):
        adminLogin()
        
    
