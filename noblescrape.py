import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_Nobel_Memorial_Prize_laureates_in_Economics'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table', {'class': 'wikitable sortable'})

for row in table.find_all('tr'):
    columns = row.find_all('td')
    for column in columns:
        print(column.text)