#Name: Alfonso Del Rosario
#Project # 3 
#Submission Date: 07/08/2021

#Correct Username: alfonso
#Correct Password: python

def VerifyUser(userID, password):
    if userID.upper() != "ALFONSO" or password.upper() != "PYTHON":
            print("incorrect username or password")
            print("=============================================")
            return False
    else:
            print("Login Successful. Welcome " + userID.upper())
            print("=============================================")
            return True

def login():
    count = 0
    while count != 3:
        id = input("Enter User ID: ")
        password = input("Enter Password: ")
        state = VerifyUser(id, password)
        
        if state == False:
            count+=1
            print("incorrect attempts " + str(count))
            if count == 3:
                print("You have failed to login 3 times. Please try again later")
        else:
            break


def about():
    print("Our mission is to produce the highest quality true random programs and make them available to the world in useful forms.")
    print("=========================================================================================================================")

def getInput():
    user = int(input("1. Login\n2. About.\n3. Quit.\nEnter Here: ")) 
    return user
            

def main():
    userInput = getInput()
    if userInput == 3:
        print("Thank You for Using Our Program")
    else:
        if userInput == 1:
            login()
        elif userInput == 2:
            about()
        else:
            print("invalid input")
            print("=============================================")
    
main()