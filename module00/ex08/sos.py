from numpy import append
import requests
from bs4 import BeautifulSoup


def scrap_morse_dict():
    web = requests.get('https://morsecode.world/international/morse2.html')
    data = web.content
    soup = BeautifulSoup(data, 'html.parser')
    tag = soup.find_all('td')
    list = []
    for i in tag:
        list.append(i.text)
    keys = []
    values = []
    for i in range(0, 72, 2):
        keys.append(list[i])
        values.append(list[i + 1])
    morse_dict = dict(zip(keys, values))
    return (morse_dict)


morse_dict = scrap_morse_dict()
print(morse_dict)
