from bs4 import BeautifulSoup
import requests
import pandas as pd
import boto3
from io import StringIO


# Set url and headers for request
url = 'https://finance.yahoo.com/quote/AMZN/history/'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}

# Send GET request to url
response = requests.get(url, headers=headers)
html_content = response.text

# Print response status to GET request
print('response.ok: {}, response.status_code: {}'.format(response.ok, response.status_code))
print('Preview of response.text: ', response.text[:700])

# Create a BeautifulSoup object to parse the HTML texts
soup = BeautifulSoup(html_content, 'html.parser')

# Find the table with the historical prices
table = soup.find('table', attrs={'data-test': 'historical-prices'})

# Extract data from each row of the table and append to csv_file list
rows = table.tbody.find_all('tr')
csv_file = []
for row in rows:
    cols = row.find_all('td')
    date = cols[0].text.strip()
    close_price = cols[4].text.strip()
    open_price = cols[1].text.strip()
    high_price = cols[2].text.strip()
    low_price = cols[3].text.strip()
    volume = cols[6].text.strip()
    csv_file.append([date, close_price, open_price, high_price, low_price, volume])

# Create dataframe from rows of gathered data
df = pd.DataFrame(csv_file, columns=['Date', 'Close', 'Open', 'High', 'Low', 'Volume'])

# Print dataframe to console before data cleaning
print(df.tail())

# Data cleaning and formattting
# Convert Date column to datetime
def convert_datetime():
    df['Date'] = pd.to_datetime(df['Date'])
    df['Date'] = df['Date'].dt.strftime('%d-%m-%Y')

# Convert Volume column to float
def convert_float():
    df['Volume'] = df['Volume'].str.replace(',', '')
    df['Volume'] = df['Volume'].astype(float)

# Run data cleaning and formatting function
convert_datetime()
convert_float()

# Print dataframe to console after data cleaning
print(df.tail())

# Write dataframe into csv file
# with open('AMZN.csv', 'w') as f:
#     df.to_csv(f, index=False)

# # Select bucket name and s3 object name
bucket_name = 'xander-test-c8'
s3_object_name = 'AMZN.csv'

#---------
# Create session with amazon bucket
s3 = boto3.client('s3', aws_access_key_id='access_key_here', aws_secret_access_key='secret_key_here')

# Create csv buffer and save dataframe to csv buffer
csv_buffer = StringIO()
df.to_csv(csv_buffer, index=False)

# Save csv file to s3 bucket
s3.put_object(Bucket=bucket_name, Key=s3_object_name, Body=csv_buffer.getvalue())
#---------

# Print message to console when csv file is saved
print('700 Datapoints saved to AMZN.csv')