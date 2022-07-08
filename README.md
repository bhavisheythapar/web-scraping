# Web Scrapping
This repository contains the file **script.py** used to scrape a list of [courses](https://www.udacity.com/courses/all?price=Free) from Udacity for the Udacity 30 day challenge created by me.

The course list and relavent information is first stored into a python dataframe and then tranfered into a SQLite database to make it easy to query the data locally. To run the file clone the repository and run the below command inside a virtual environemnt.

```pip install -r requirements.txt```

Once all tthe dependencies are installed simply run the python script using the command below.

```python script.py```
