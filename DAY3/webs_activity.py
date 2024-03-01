import requests
from bs4 import BeautifulSoup
import pandas as pd

# Fetching the HTML content
html_text = requests.get("https://www.scrapethissite.com/pages/simple/")
souped_html = BeautifulSoup(html_text.text, "lxml")

# Extracting country names, capitals, populations, and areas
countries = [country.text.strip() for country in souped_html.find_all("h3")]
capitals = [capital.text.strip() for capital in souped_html.find_all(class_="country-capital")]
populations = [population.text.strip() for population in souped_html.find_all(class_="country-population")]
areas = [area.text.strip() for area in souped_html.find_all(class_="country-area")]

# Creating dataframes for each attribute
df_countries = pd.DataFrame(countries, columns=["Countries"])
df_capitals = pd.DataFrame(capitals, columns=["Capital"])
df_populations = pd.DataFrame(populations, columns=["Population"])
df_areas = pd.DataFrame(areas, columns=["Area (km^2)"])

# Concatenating dataframes horizontally
df = pd.concat([df_countries, df_capitals, df_populations, df_areas], axis=1)

print(df)

df.to_excel("countries_data.xlsx")