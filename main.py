import re
import requests
from bs4 import BeautifulSoup
page = requests.get("https://www.udacity.com/courses/all?price=Free",verify=False)
soup = BeautifulSoup(page.content, 'html.parser')
ul=soup.find('ul', {'id': 'catalog-v2_results__1FjDi'})
print(ul)
# children = ul.findChildren("a" , recursive=False)
# for child in children:
#     print(child)
# for item in soup.findAll('ul',{'class':'catalog-footer_linkGroupItems__1wmH6'}):
#     print(item)

# for item in soup.findAll('div',{'class':'container_contain__2hCQ1'}):
#     sub_items = item.findAll('li',{'class':'href text'})
#     for sub_item in sub_items:
#         print(sub_item)