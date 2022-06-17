# This program will write to a .txt file all the article titles on the NY Times homepage.

import requests
from bs4 import BeautifulSoup
    

get_site = requests.get('https://www.nytimes.com/')
site_content = BeautifulSoup(get_site.content, 'html.parser')
article_text = site_content.find_all('h3', class_="indicate-hover")
count = 0

with open('ny_times_headlines.txt', 'w') as txt_file:
    for hl in article_text:
        txt_file.write(article_text[count].get_text() + '\n')
        count += 1