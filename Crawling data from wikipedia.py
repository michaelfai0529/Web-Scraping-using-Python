# import the Beautiful Soup and request package for Web Scraping
from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

# Create an object that contain the text data , parsing the data in html tag
soup = BeautifulSoup(page.text,'html')

#<table class="wikitable sortable">

# t1 is the object that contain the data of table tag and the wanted class
table = soup.find('table', class_ = "wikitable sortable" )
# retrun the title information we want
title = table.find_all('th')
# use list comprhension to create a list of title
wtt = [th.text.strip() for th in title]

print(wtt)

import pandas as pd
df = pd.DataFrame(columns= wtt)
print(df)

#extract all tr in the table object
tr = table.find_all('tr')

#loop and extract the <td> element in the (column_data object = <tr>)

for row in tr[1:]: # get rid of the 1st empty column
    td = row.find_all('td')
    # make a list comprehension in the <td> tag that reformat the data
    i_row_data = [data.text.strip() for data in td]
    print(i_row_data)
    length = len(df)
    df.loc[length] = i_row_data

print(df)

df.to_csv(r'C:\Users\02008552\OneDrive - pccw.com\Desktop\Python project\Web crawling\company_revenue', index = False)




