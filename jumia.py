import requests
from bs4 import BeautifulSoup
import pandas as pd

jumia_page = requests.get("https://www.jumia.co.ke/")
jumia_soup = BeautifulSoup(jumia_page.content, "html.parser")

# Define the indices of the items you want to extract
item_indices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

data = []

for index in item_indices:
    item = jumia_soup.find_all("div", class_="itm col")[index].get_text().strip()
    price = jumia_soup.find_all("div", class_="prc")[index].get_text().strip()
    data.append([item, price])

# Create DataFrame from the scraped data
df = pd.DataFrame(data, columns=["Product", "Price"])

# Save DataFrame to CSV file
df.to_csv("jumia_products.csv", index=False)

print("CSV file created successfully!")
