import sqlite3

class User:
    def __init__(self,username, ID, Fname, Lname):
        self.username = username
        self.ID = ID
        self.Fname = Fname
        self.Lname = Lname


def createCentroids(k, dict):
    pass

def main():
    k = 8
    pointsDict = {}
    createCentroids(k, pointsDict) #Ideally you would want to run the function using a range of Ks and see where a sudden dip would happen.

main()