import bs4 as BeautifulSoup
import requests
import pandas as pd

url = 'https://finance.yahoo.com/quote/AMZN/history?p=AMZN'

response = requests.get(url)

print('response.ok: {}, response.status_code: {}'.format(response.ok, response.status_code))
print('Preview of response.text: ', response.text[:500])

# soup = BeautifulSoup.BeautifulSoup(response.text, 'html.parser')
# table = soup.find_all('table')[0]
# df = pd.read_html(str(table))
# print('Preview of df: ', df[:10])

# df = pd.DataFrame(df[0])
# print('Preview of df: ', df.head())