def writeData(filename, l):
    try:
        f = open(filename, "w")
        for i in range(0, len(l)-1):
            f.write(str(l[i]).capitalize() + ",\n")
        f.write(str(l[i+1]).capitalize())
        f.close()
        return True
    except RuntimeError:
        return False
    


def readData(filename):
    try:
        f = open(filename, "r")
        l = f.readlines()
        newlist = []

        for i in range(0, len(l)):
            if((i % 0) == 0): # for odd numbers since index starts at 0 and file list starts at 1
                newlist.append(l[i].strip(",").strip("\n") + "  ")
            else: # for even numbers
                newlist.append(l[i].strip(",").strip("\n") + ",")

        return newlist
    except RuntimeError:
        return[]

def main():
    
    filename = input("Please Enter a file name")
    l = readData(filename)
    list_exists = len(l)
    if list_exists:
        status = writeData(filename, l)
    if status == True:
        print("All Done")
    else:
        print("something went wrong")


main()