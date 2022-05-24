from curses.ascii import isalnum
import sys
from numpy import append
import requests
from bs4 import BeautifulSoup


def check_str_is_alnum(str):
    for i in range(0, len(str)):
        if str[i] == ' ':
            continue
        elif str[i].isalnum() is False:
            print_error()
            quit()


def print_error():
    if n_arg != 0:
        print('Error !')
    print('Usage : python3 sos.py [arg_i] ...')
    print('arg strings should only contain alphanumeric characters or space.')


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


arg_list = sys.argv[1:]
n_arg = len(arg_list)
if n_arg == 0 or n_arg < 1:
    print_error()
else:
    str = ' '.join(arg_list)
    check_str_is_alnum(str)
    str = str.replace(" ", "/")
    str = str.upper()
    morse_dict = scrap_morse_dict()
    morse_lst = []
    for i in range(0, len(str)):
        if str[i] == '/':
            morse_lst.append('/')
        else:
            morse_lst.append(morse_dict[str[i]])
    morse_str = ' '.join(morse_lst)
    print(morse_str)
