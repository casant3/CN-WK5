from bs4 import BeautifulSoup
import requests
import pandas as pd

html_text = requests.get("http://127.0.0.1:5500/test2.html")

souped_html = BeautifulSoup(html_text.text,"lxml")

countries = souped_html.find_all("h3")