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

