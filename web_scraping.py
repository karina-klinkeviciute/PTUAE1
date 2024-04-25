import csv
from time import sleep

import requests
from bs4 import BeautifulSoup

source = requests.get('https://www.autoplius.lt/').text
sleep(10)

soup = BeautifulSoup(source, 'html.parser')

blocks = soup.find_all('a', class_='promoted-announcement')

# print(block.prettify())
sum_prices = 0
count_prices = 1
with open("ads_data.csv", "w") as file:
    csv_writer = csv.writer(file)
    for block in blocks:
        price = block.find('div', class_='body-price')
        name = block.find('div', class_='body-description-line1')
        if price is not None:
            try:
                price = int("".join(price.text.strip().strip("€").strip().split(" ")))
                sum_prices += price
                count_prices += 1
            except ValueError:
                pass

            print(price)

        csv_writer.writerow([name.text, price, ])

average = sum_prices/count_prices
#
# print("Average price for promoted vehicles: ", average)
#
# # div = soup.find("div", {"id": "articlebody"})
# #
# # print(div.prettify())
#
#
# source = requests.get('https://www.skelbiu.lt/').text
# sleep(10)
#
# soup = BeautifulSoup(source, 'html.parser')
#
# blocks = soup.find_all('a', class_='promoted-announcement')

# print(block.prettify())
#
# source = requests.get('https://www.lemongym.lt/en/group-trainings/').text
#
# soup = BeautifulSoup(source, 'html.parser')
#
# link_elements = soup.find_all('a', class_='card-simple')
#
# for link_element in link_elements:
#     sleep(2)
#     link = link_element["href"]
#     print(link)
#     page = requests.get(link).text
#     page_soup = BeautifulSoup(page, "html.parser")
#     print(page_soup.prettify())
#     contents = soup.find("div", class_="content-details-layout__content")
#     if contents is not None:
#         print(contents.text)

