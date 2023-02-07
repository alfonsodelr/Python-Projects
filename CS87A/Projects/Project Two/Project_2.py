#Name: Alfonso Del Rosario
#Project: 2
#Submission Date: 07/04/2021

#function to convert and print the two values: Celsius and Fahrenheit
def tempConvert(Fahrenheit):
    print("Celsius: %.2f\nFahrenheit: %.2f\n" % ((5/9*(Fahrenheit - 32)), Fahrenheit)) #Prints converted value of Celsius and passed value of Fahrenheit

#function to convert speed from mph and print the two values miles/second and miles/hour
def speedConvert(mph):
    print("mile(s)/second: %.2f\nmile(s)/hour: %.2f\n" % ((mph/60), mph)) #Prints converted value of mile(s) per second and passed value of mile(s) per hour

#void function that greets out the user
def goodbye():
    print("Thank you for using our program")

#main function
def main():
    
    userInput = int(input("Enter [1] to convert Fahrenheit temperature to Celsius\nEnter [2] to convert speed from miles per hour to meters per second\nEnter Here: ")) #asks for input from user
    if userInput == 1: #test if the user wants to convert temp
        tempInput = float(input("Enter the temperature you wish to convert to Celsius: ")) #asks for what temperature the user wants to convert
        tempConvert(tempInput) #calls the tempConvert function and passes it the value of tempInput for calculation
    elif userInput == 2: #tests if the user wants to convert speed
        speedInput = float(input("Enter the speed in miles/hour you wish to input: ")) #asks for what speed the user wants to convert
        speedConvert(speedInput) #calls the speedConvert function and passes speedInput for calculation
    else: #tests if the user entered something invalid
        print("Invalid Input\n") #notifies the user that input was invalid

main() #calls main function
goodbye() #calls goodbye function
