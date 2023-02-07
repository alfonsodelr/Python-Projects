#This program parses through a Unity class through their unity documentation. 
#It finds all instances of a td tag with class lbl and within that tag it finds the contents of its anchor tag.
#This serves the purpose of listing all the class properties and methods. 

import requests
from bs4 import BeautifulSoup

def main():
    test = requests.get('https://docs.unity3d.com/ScriptReference/Transform.html')

    soup = BeautifulSoup(test.content, 'html.parser')

    layer_1 = soup.findAll("td", attrs={"class": "lbl"})

    for i in layer_1:
        layer_2 = i.find("a")
        print(layer_2.contents[0])

main()

