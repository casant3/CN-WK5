# from bs4 import BeautifulSoup
# import requests
# import pandas as pd

# html_text = requests.get("https://www.scrapethissite.com/pages/simple/")
# # print(html_text.text)

# souped_html = BeautifulSoup(html_text.text,"lxml")

# countries = souped_html.find_all("h3")

# # print(countries)

# # for country in countries:
# #     print(country.text.strip())
    
# # print([country.text.strip() for country in countries])
# df0 = pd.DataFrame([country.text.strip() for country in countries])

# print(df0)

# countries_capitals = souped_html.find_all(class_="country-capital")
# # print(countries_capitals)

# # for capital in countries_capitals:
#     # print(capital.text)
    
# df1 = pd.DataFrame([capital.text.strip() for capital in countries_capitals])

# print(df1)

# countries_populations = souped_html.find_all(class_="country-population")

# df2 = pd.DataFrame([population.text.strip() for population in countries_populations])

# print(df2)


# countries_area = souped_html.find_all(class_="country-area")

# df3 = pd.DataFrame([area.text.strip() for area in countries_area])

# print(df3)

# df = pd.DataFrame({
#     "Countries": df0,
#     "Capital": df1,
#     "Population": df2,
#     "Area (km^2)": df3
#     })

# print(df)

# from bs4 import BeautifulSoup
# import requests
# import pandas as pd

# html_text = requests.get("https://www.scrapethissite.com/pages/simple/")
# soup = BeautifulSoup(html_text.content, "html.parser")

# countries_data = []
# for country in soup.find_all("div", class_="country"):
#     country_name = country.h3.text.strip()
#     country_capital = country.find(class_="country-capital").text.strip()
#     country_population = country.find(class_="country-population").text.strip()
#     country_area = country.find(class_="country-area").text.strip()
#     countries_data.append([country_name, country_capital, country_population, country_area])

# df = pd.DataFrame(countries_data, columns=["Country", "Capital", "Population", "Area (km^2)"])
# print(df)

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

# my_file = open("test2.html", "r")

# souped_html = BeautifulSoup(my_file, "lxml")

# print(my_file)
 