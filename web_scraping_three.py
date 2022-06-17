import requests
from bs4 import BeautifulSoup

def print_to_text(base_url):
    """
    :param base_url: URL of article to scrape
    :return: naked content to text file
    """
    r = requests.get(base_url)
    soup = BeautifulSoup(r.text, 'html.parser')
    with open("work less.txt", "w") as textfile:
        for paragraph in soup.find_all(class_='body__inner-container'):
            textfile.write(paragraph.text.replace("<div>",""))

if __name__ == "__main__":
    #Chose my own article
    base_url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
    
    print_to_text(base_url)
    