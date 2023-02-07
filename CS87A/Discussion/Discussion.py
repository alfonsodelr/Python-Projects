import re

def main():
    check = "[a-z]\d|\s" 
    user_input = input()
    if(re.findall(check, user_input)):
        print('Satisfied')
    else:
        print('Not Satisfy')


main()