#Name: Alfonso Del Rosario
#Submission Date: 10/17/2021
#Assignmnet # 4

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def read_file(fileName, x):

    if x == 0: #returns values for x axis
        f=open(fileName, 'r')

        line = f.readlines()
        left = []

        for i in range(0, len(line)):
            new_list = line[i].split()
            cut = ''
            for j in range (0,3): #Cuts city names into the first 3 letters to remove clutter
                cut += new_list[0][j]
                if i > 1: #To avoid out of bounds access
                    if cut == left[i-1]: #if the cut version of the previous city is the same
                        cut+='(1)' #then add a (1) to avoid duplication, 
                                   #which would make the plot stack both cities
                    
            left.append(cut)

        return left
    else: #returns values for y axis
        f=open(fileName, 'r')

        line = f.readlines()
        right = []

        for i in range(0, len(line)):
            new_list = line[i].split()
            conv = float(new_list[1])
            right.append(conv)

        return right


def main():

    done = False

    while(not(done)):
        num = int(input("===============================\n\nMENU - (Please enter a number)\n1. Plot with BOTH sets shown in one plane\n2. Plot with sets separated into different planes.\
This plot also shows min and max data items\n3. This plot produces an estimate of the amount of rain in inches after (input) amount of years from the initial year using the trend\
from the two data sets we were provided.\n0. Exit\n\nEnter Here: "))

        if num == 1:

            left = read_file("rainfallSet1.txt", 0)
            right = read_file("rainfallSet1.txt", 1)
            right_2 = read_file("rainfallSet2.txt", 1)

            fig = plt.figure()
            ax = fig.add_subplot(1,1,1)

            ax.bar(left, right, color = 'b' , width=0.5)
            ax.bar(left, right_2, color = 'g' , width=0.5)
            ax.legend(labels=['Rainfall (inches)', 'After 10 Years'])
            ax.set_ylabel('Rainfall (inches)')

            plt.savefig('Part1.jpg')
            plt.show()
            

        elif num == 2:

            left = read_file("rainfallSet1.txt", 0)
            right = read_file("rainfallSet1.txt", 1)
            right_2 = read_file("rainfallSet2.txt", 1)

            fig, (a1, a2) = plt.subplots(2)
            ax = plt.gca()
            ax.set_ylim([0, 100])

            clrs = ['blue' if (x == max(right)) else 'red' if (x == min(right)) else 'grey' for x in right ]
            a1.bar(left,right, color=clrs)
            a2.bar(left, right_2, color=clrs)
            minimum = mpatches.Patch(color='red', label='min')
            maximum = mpatches.Patch(color='blue', label='max')

            a1.legend(handles = [minimum, maximum])
            a1.set_ylabel('Rainfall (inches)')
            a2.legend(handles = [minimum, maximum])
            a2.set_ylabel('Rainfall (inches)')
            a2.set_title('After 10 Years')

            plt.savefig('Part2.jpg')
            plt.show()
            

        elif num == 3:
            user_input = int(input("Enter How Many Years After Base Year You Would Like To Check: "))

            left = read_file("rainfallSet1.txt", 0)
            right = read_file("rainfallSet1.txt", 1)
            right_2 = read_file("rainfallSet2.txt", 1)
            new_right = []

            for i in range(0 , len(left)):
                difference = right[i] - right_2[i]
                new_right.append(right[i] - (difference * (user_input/10.0)))

            fig = plt.figure()
            ax = fig.add_subplot(1,1,1)

            ax.bar(left, new_right, color = 'b' , width=0.5)
            ax.legend(labels=['Rainfall (inches)', 'After 10 Years'])
            ax.set_ylabel('Rainfall (inches)')
            ax.set_ylim([0, 100])
            string = 'After ' + str(user_input) + ' Years'
            ax.set_title(string)

            plt.savefig('Part3.jpg')
            plt.show()
        else:
            print("Thank You For Using My Program")
            done = True

main()