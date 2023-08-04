import pandas as pd
import configparser
from newsapi import NewsApiClient
import datetime as dt

config = configparser.ConfigParser()
config.read('config.ini')

key = config['NewsAPI']['key']

# print(key)

newsapi = NewsApiClient(api_key=key)

data = newsapi.get_everything(q="covid",language='en',page_size=20)

print(data.keys())


print(data['articles'][0])

articles = data['articles']

for x,y in enumerate(articles):
    print(f'{x} {y["title"]}')


df = pd.DataFrame(articles)

df.to_csv('covidNewsData.csv')