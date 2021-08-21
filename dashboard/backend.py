import os
import ast
import re
import tweepy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import re
import json

#from textblob import TextBlob
#from wordcloud import WordCloud
#import seaborn as sns
#sns.set(style='ticks', palette='Set2')
# %matplotlib inline

with open('api_info.txt', 'r') as f:
  data = f.read().replace('\n', '')
api_dict = json.loads(data)

consumer_key = api_dict["consumer_key"]
consumer_secret = api_dict["consumer_secret"]
access_token = api_dict["access_token"]
access_secret = api_dict["access_secret"]
api_dict.clear()

"""### Authenticate + Init API obj"""

authenticate = tweepy.OAuthHandler(consumer_key,consumer_secret)
authenticate.set_access_token(access_token,access_secret)
api = tweepy.API(authenticate,wait_on_rate_limit=True)

## List of fintwit users
fintwit_users = [
    'BahamaBen9',
    'HedgeMind',
    'StockDweebs',
    'hhhypergrowth',
    'traderstewie',
    'cperruna',
    'richard_chu97',
    'Beth_Kindig',
    'BrianFeroldi',
    'BackpackerFI',
    'JonahLupton'
]

#list comprehension to flex
all_tweets = [api.user_timeline(screen_name=user_handle, count=200,lang='en',tweet_mode='extended') for user_handle in fintwit_users]
