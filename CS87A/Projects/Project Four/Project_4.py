#Name: Alfonso Del Rosario
#Project 4
#Submission Date: 07/18/2021

#========================================================================#

#takes a string as input and converts it into a ciphered string using the 
#doubled ascii value of the first element as a key
def cipher(word): 
    key = ord(word[0])
    newWord = chr(key + key)

    for i in range(1, len(word)): #loops through all characters in string
        newWord += chr(ord(word[i]) + key) #converts to a new character using key
    
    return newWord #returns ciphered string

#gets the original key by dividing the ascii value of the first element
#by two and uses the key to decipher the hidden text
def decipher(word):
    key = int((ord(word[0]))/2)
    original = chr(key)

    for i in range(1, len(word)): #loops through all characters in string
        original += chr(ord(word[i]) - key) #converts to original string

    return original #returns deciphered string

def main():
    password = input("||Enter a word to cipher||\n\nEnter Here: ")
    ciphered = cipher(password)
    deciphered = decipher(ciphered)
    print("Ciphered Version: " + ciphered)
    print("Deciphered Version: " + deciphered)

main()