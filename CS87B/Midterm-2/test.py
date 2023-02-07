import matplotlib.pyplot as plt
import re

def fileToDict(fname):
    f = open(fname, 'r')
    arr = f.readlines()
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    num_regex = r'[0-9]+'

    emails = []
    nums = []
    invalid_email = 'invalid@email.com'

    for i in range(0, len(arr)):
        l = arr[i]
        l = l.strip('\n')
        new_arr = l.split(' ')
        #################################
        if(re.fullmatch(regex, new_arr[0])):
            emails.append(new_arr[0])
        else:
            emails.append(invalid_email)
        ##################################
        temp_arr = []                    
        for j in range(1,len(new_arr)):
            if(re.fullmatch(num_regex, new_arr[j])):
                temp_arr.append(new_arr[j])
            else:
                temp_arr.append('invalid')
        nums.append(temp_arr)

    d = {}
    for i in emails:
        for j in nums:
            d[i] = j
            nums.remove(j)
            break
    
    return d

def cleanUp(myDict):
    for k in myDict:
        for i in range(len(myDict[k])):
            if (myDict[k][i] == 'invalid'):
                myDict[k][i] = '0'
            else:
                continue

    for k in myDict:
        for i in range(len(myDict[k])):
                myDict[k][i] = int(myDict[k][i])
    
    nums = []
    emails = []
    for k in myDict:
        emails.append(k)
        sum = 0
        for i in range(len(myDict[k])):
            sum += myDict[k][i]
        nums.append(sum)

    d = {}
    for i in emails:
        for j in nums:
            d[i] = j
            nums.remove(j)
            break
    
    return d

def myPlot(myDict):
    nums = []
    emails = []
    for k in myDict:
        emails.append(k)
        nums.append(myDict[k])
    
    fig = plt.figure()

    plt.bar(emails, nums, color='blue')
    plt.xlabel("Emails")
    plt.ylabel("Sum of values")
    plt.title("Midterm")

    return fig

def main():
    filename = input('Enter File Name Here: ')
    d = fileToDict(filename)
    new_d = cleanUp(d)
    fig = myPlot(new_d)

    fig.show()
    user_input = input('Do you wish to save this figure? [Y] - Yes || [N] - No\nEnter Here: ')
    if(user_input.upper() == 'Y'):
        fig.savefig('plot.png')
        print('You have chosen to save the figure. Thank You For Using My Program')
    else:
        print('You have chosen NOT to save the figure. Thank You For Using My Program')

main()