import requests
from bs4 import BeautifulSoup

def main():
    test = requests.get('https://valorant.fandom.com/wiki/Agents')

    soup = BeautifulSoup(test.content, 'html.parser')

    layer_1 = soup.findAll("img", attrs={"height" : "24", "width" : "24", "class" : "lazyload"})
    l = []

    for i in range (0, len(layer_1)):
        l.append(str(layer_1[i]))

    print(l[0])

main()
