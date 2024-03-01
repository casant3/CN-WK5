from bs4 import BeautifulSoup
import requests
import pandas as pd

rating_to_int = {
    "One" : 1,
    "Two" : 2,
    "Three" : 3,
    "Four" : 4,
    "Five" : 5,
}

title_collection = []
price_collection = []
rating_collection = []

for i in range(1,51):
    url = f"http://books.toscrape.com/catalogue/page-{i}.html"
    html_text = requests.get(url).text

    soup = BeautifulSoup(html_text, 'lxml')
    titles = soup.find_all('h3')


    for book_title in titles:
        # print("Title : ", book_title.find('a').get('title').strip())
        title = book_title.find('a').get('title').strip()
        title_collection.append(title)
        price = book_title.find_next('p', class_="price_color").text.strip('Â£')
        # print("Price: ", price.text.strip('Â'))
        price_collection.append(float(price))
        rating = book_title.find_previous('p', class_='star-rating').get('class')[1]
        # print(rating_to_int.get(rating))
        rating_collection.append(rating_to_int.get(rating))

df = pd.DataFrame({
    "Title" : title_collection,
    "Price": price_collection,
    "Rating / 5" : rating_collection
})

# print(df)

df.to_excel("Books1.xlsx", index=False)

max_price = max(df["Price"])
print(f"max price of a boook is £{max_price}")

rating_4 = (df["Rating / 5"] == 4).sum()
print(f"There are {rating_4} 4* rated books")

sum_price = df["Price"].sum()
mean = round((sum_price / 1000), 2)#also can use .mean()
print(f"The mean price for a book is £{mean}")