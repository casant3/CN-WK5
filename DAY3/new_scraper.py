import requests
from bs4 import BeautifulSoup
import pandas as pd

html_text = requests.get("https://wearecodenation.com/2024/01/23/data-course-playground/")
soup = BeautifulSoup(html_text.text, "lxml")

h5s = soup.find_all("h5", class_="elementor-heading-title elementor-size-default")

course_dict = {}

for h5 in h5s:
    if ":" in h5.text:
        course_title = h5.text.strip()
        dates = h5.find_next("h6").text.strip()
        course_dict[course_title] = dates 
        
print(course_dict)

#Activity 2

df = pd.DataFrame(list(course_dict.items()), columns=['Course Title', 'Date'])

print(df)


df.to_excel('course_dates.xlsx', index=False)
            
