import datetime

def exercise():
    print("Enter the exercise completed by {}:".format(name))
    ex= input()
    def data_of_exercise():
        return "[{}] - {}".format(getdate(),ex)
    print(data_of_exercise())  
    if(name=="Rohan"):
        fp = open("client1_ex.txt","a+")
        fp.write(data_of_exercise()+"\n")
        fp.close()
        print("Exercise data entered successfully!!")
    elif(name=="Sukesh"):
        fp = open("client2_ex.txt","a+")
        fp.write(data_of_exercise()+"\n")
        fp.close()
        print("Exercise data entered successfully!!")
    elif(name=="Arthuro"):
        fp = open("client3_ex.txt","a+")
        fp.write(data_of_exercise()+"\n")
        fp.close()
        print("Exercise data entered successfully!!")
    else:
        pass

def get_exercise_data():
    try:
        if(get==1):
            fp = open("client1_ex.txt","r")
            p = fp.readlines()
            for data in p:
                print(data)
            fp.close()
        elif(get==2):
            fp = open("client2_ex.txt","r")
            p = fp.readlines()
            for data in p:
                print(data)
            fp.close()
        elif(get==3):
            fp = open("client3_ex.txt","r")
            p = fp.readlines()
            for data in p:
                print(data)
            fp.close()
        else:
            print("Please select the right opertion")
    except:
        print("The File is empty!...\nPlease enter the data first:)")

def diet():
    print("Enter the items taken under Diet by {}:".format(name))
    di= input()
    def data_of_diet():
        return "[{}] - {}".format(getdate(),di)
    print(data_of_diet()) 
    if(name=="Rohan"):
        fp = open("client1_di.txt","a+")
        fp.write(data_of_diet()+"\n")
        fp.close()
        print("Diet data entered successfully!!")
    elif(name=="Sukesh"):
        fp = open("client2_di.txt","a+")
        fp.write(data_of_diet()+"\n")
        fp.close()
        print("Diet data entered successfully!!")
    elif(name=="Arthuro"):
        fp = open("client3_di.txt","a+")
        fp.write(data_of_diet()+"\n")
        fp.close()
        print("Diet data entered successfully!!")
    else:
        pass 
def get_diet_data():
    try:
        if(get==1):
            fp = open("client1_di.txt","r")
            p = fp.readlines()
            for data in p:
                print(data)
            fp.close()
        elif(get==2):
            fp = open("client2_di.txt","r")
            p = fp.readlines()
            for data in p:
                print(data)
            fp.close()
        elif(get==3):
            fp = open("client3_di.txt","r")
            p = fp.readlines()
            for data in p:
                print(data)
            fp.close()
        else:
            print("Please select the right opertion")
    except:
        print("The File is empty!...\nPlease enter the data first:)")

def getdate():
     return datetime.datetime.now()

while(True):
    name= ""
    print("\n---------------------------")
    print("------WELCOME TO HMS------")
    print("---------------------------")
    print("What brings you here? \n1. To enter your exercise/diet data\n2. To read exercise/diet data?\n3. Or do you want to quit :(")
    choice = int(input("Your choice: "))
    if(choice==1):
        print("Select client from the below list:")
        print("1. Rohan \n2. Sukesh \n3. Arthuro \n4. EXIT")
        i = int(input("Enter your choice : "))
        if(i==1):
            name= "Rohan"
        elif(i==2):
            name= "Sukesh"
        elif(i==3):
            name= "Arthuro"
        elif(i==4):
            exit(0)
        else:
            print("Please enter the valid choice!")
            exit(0)
        print("------------------------")
        print("Select the option below to enter the data ")
        print("1. EXERCISE \n2. DIET \n")
        j = int(input("Enter your choice : "))
        if(j==1):
            exercise()
        elif(j==2):
            diet()
        else:
            print("You have entered wrong choice!")
            pass
    elif(choice==2):
        print("Select client from the below list:")
        print("1. Rohan \n2. Sukesh \n3. Arthuro \n")
        get = int(input("Enter your choice : "))
        print("-------------------------")
        print("Select the option below to get the data ")
        print("1. EXERCISE \n2. DIET \n")
        get2 = int(input("Enter your choice : "))
        if(get2==1):
            get_exercise_data()
        elif(get2==2):
            get_diet_data()
        else:
            print("You have entered wrong choice!")
            pass
    elif(choice==3):
        print("Sorry if we have caused any inconvinience.\nBYE..!")
        exit(0)
    else:
        print("You have entered wrong choice!")
        exit(0)
