# Web Scraping (Udacity 30 Day Challenge)

Follow the tutorial for this repository on my Medium [article](https://medium.com/@bhavisheythapar/the-udacity-challenge-15-courses-in-one-month-part-1-6881ead609f2#:~:text=My%20initial%20plan%20was%20to%20pull%203%20pieces%20of%20information%20from%20the%20website%20that%20would%20better%20help%20me%20select%20the%20courses%20I%20want%20to%20enroll%20in%20and%20they%20are%2C).

This repository contains the file **script.py** used to scrape a list of free [courses](https://www.udacity.com/courses/all?price=Free) and their relavent information from Udacity for the [Udacity 30 day challenge](https://medium.com/@bhavisheythapar/the-udacity-challenge-15-courses-in-one-month-part-1-6881ead609f2) created by me. The information is first stored in a python dataframe and then transferred into a database to make it easy to query the data locally.

To run the program, clone the repository and run the below command inside a virtual environment. SQLite needs to be installed [separately](https://www.sqlite.org/download.html). 

```pip install -r requirements.txt```

Once all the dependencies are installed  run the python script in the terminal using the command below.

```python script.py```
