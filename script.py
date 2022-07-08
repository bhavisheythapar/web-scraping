import time
import pandas as pd
import sqlite3
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Web scraping
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
 
driver.get('https://www.udacity.com/courses/all?price=Free')
driver.maximize_window()
time.sleep(3)
soup = BeautifulSoup(driver.page_source, 'lxml')
time.sleep(3)

title_list=[]
duration_list=[]
summary_list=[]
level_list=[]

for course in soup.select('.catalog-v2_results__1FjDi > li'):

    title=course.select_one('.card_title__35G97').text
    duration=course.select_one('.card_duration__1hWII').text
    summary=course.select_one('.card_summary__1HlQ7').text
    level=course.select_one('.card_level__2HNxe').text

    title_list.append(title)
    duration_list.append(duration)
    summary_list.append(summary)
    level_list.append(level)

# Create dataframe and transfer data to it.
df=pd.DataFrame(
    {'title': title_list,
     'duration': duration_list,
     'summary': summary_list,
     'level': level_list
    })

# Create a database and transfer data to it.
conn = sqlite3.connect('Udacity')
c = conn.cursor()
conn.commit()
df.to_sql('courses', conn, if_exists='replace', index = True)