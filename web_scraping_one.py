# This program scrapes the NY Times website main page for all the headliners titles

import requests
from bs4 import BeautifulSoup

get_site = requests.get('https://www.nytimes.com/')
site_content = BeautifulSoup(get_site.content, 'html.parser')
headliners_html = site_content.find_all(class_='css-xdandi')
count = 0

for x in headliners_html:
    x = headliners_html[count].get_text()
    count += 1
    print(x)