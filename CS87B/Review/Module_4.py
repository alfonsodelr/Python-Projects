import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def main():
    f=open('rainfallSet2.txt', 'r')

    line = f.readlines()
    l = []

    for i in range(0, len(line)):
        l.append(line[i].split())

    left = []
    right = []

    for i in range (0, len(l)):
        left.append(l[i][0])
        right.append(l[i][1])

    print(left)
    print(right)

    new_right = []

    for i in range (0, len(right)):
        conv = float(right[i])
        new_right.append(conv)
    
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.bar(left,new_right, color='b', width=0.5)
    ax.legend(labels=['Rainfall (inches)','After 10 Years'])
    ax.set_ylabel('Rainfall (Inches)')

    plt.show()

main()