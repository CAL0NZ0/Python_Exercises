import requests
from bs4 import BeautifulSoup

def get_list():
    base_url = input("Enter URL: ")
    file_name = input("Enter new file name: ")
    get_site = requests.get(base_url)
    site_html = BeautifulSoup(get_site.content, 'html.parser')
    name_lst = list(site_html)
    lst = []    
    
    with open(file_name + ".txt", 'w') as file:
        for x in name_lst:
           file.write(x)
           
    with open(file_name+'.txt', 'r') as file:
        num_lst = list(file)
        for x in num_lst:
            lst.append(int(x))
    return lst
           
        
def lst_comp():
    prime_nums = get_list()
    happy_nums = get_list()
    same_nums = []
    
    for num in prime_nums:
        if num in happy_nums and num not in same_nums:
                same_nums.append(num)
    print(same_nums)
            
       
lst_comp()

           



