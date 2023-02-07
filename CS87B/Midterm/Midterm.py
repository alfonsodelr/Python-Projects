import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import requests
from bs4 import BeautifulSoup
import re

def pause():
    nice = input()

def fileToDict(fname):
    f = open(fname, 'r')
    arr = f.readlines()
    #cleanUp(arr)

    for i in range(0, len(arr)-1):
        l = arr[i].split()
        print[l]

    pause()

def cleanUp(data):
    new_list = []

    for i in range(0, len(data)):
        l = data[i].split()
        print[l]

    print(new_list)

def main():
    #filename = input('Enter File Name Here: ')
    fileToDict('testing.txt')
    
    


main()