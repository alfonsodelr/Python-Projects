#Alfonso Del Rosario
#Assignmnet 7 

import requests
import json
import re

#This program asks the customer for a desired letter and uses regex to filter the names of the 
#currency by their first letter and stores these values in an existing/non-existing text file. 

def menu():
    print('''
    [1] - Print Filtered List and Store in Text File
    [2] - Print All
    [0] - Exit
    ''')

def main():
    url = 'https://api.coinbase.com/v2/currencies'
    r = requests.get(url)
    j = r.json()
    noFilter = r'^[A-Z].*'
    toFilter = '.*'
    done = False

    while(not(done)):
        menu()
        menuChoice = int(input())

        if(menuChoice == 0):
            done = True
            print('Program Exit')

        elif(menuChoice == 1):

            userInput = input('Enter Letter To Filter Here: ')
            filtered = userInput.upper() + toFilter

            for item in j["data"]:
                if(re.fullmatch(filtered, item['name'])):
                    print('Name: ', item['name'], '\nID: ', item['id'], '\n' )
                else:
                    continue
            
            f = open('myfile.txt', 'w') #opened with 'w' to reset the text file everytime a different letter is used to filter
            f.close()

            f = open('myfile.txt', 'a') 

            f.write('All Currencies Starting With [' + userInput.upper() + ']\n\n')
            
            for item in j["data"]:
                if(re.fullmatch(filtered, item['name'])):
                    temp = 'Name: ' + item['name'] + '\nID: ' + item['id'] + '\n'
                    f.write(temp)
            
        elif(menuChoice == 2):
            for item in j["data"]:
                if(re.fullmatch(noFilter, item['name'])):
                    print('Name: ', item['name'], '\nID: ', item['id'], '\n' )
                else:
                    continue

        else:
            print('Invalid Input')

    

main()
