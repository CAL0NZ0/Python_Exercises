# This program takes a list of names and counts how many of each name on the list and print out the name with amount.

import requests
from bs4 import BeautifulSoup

def write_list():
    get_site = requests.get('https://www.practicepython.org/assets/nameslist.txt')
    site_html = BeautifulSoup(get_site.content, 'html.parser')
    name_lst = list(site_html)
    
    with open('name_list.txt', 'w') as file:
        for x in name_lst:
           file.write(x)
           

    
def read_lst():
    darth = 0
    lea = 0
    luke = 0
    with open('name_list.txt', 'r') as file:
        all_names = list(file)
        for x in all_names:
            x = x.replace('\n','').lower()
            if x == 'darth':
               darth += 1 
            elif x == 'lea':
                lea += 1
            else:
                luke += 1
        print('This list contains Darth',darth,'times, Lea', lea,'times and Luke',luke,'times.')
                              

                
write_list()
read_lst()