import requests
from bs4 import BeautifulSoup
page = requests.get("https://www.udacity.com/courses/all?price=Free",verify=False)
soup = BeautifulSoup(page.content, 'html.parser')
# a=soup.find(id="#content")
# b=a.find_all(class_="catalog-v2_page__187xz")
# c=b.find_all(class_="container_contain__2hCQ1")
# d=c[0].find_all(class_="catalog-v2_results__1FjDi")
for ultag in soup.find_all('ul', {'class': 'catalog-v2_results__1FjDi'}):
    for litag in ultag.find_all('li'):
        print (litag.text)

