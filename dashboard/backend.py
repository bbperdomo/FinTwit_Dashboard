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


#this is the magic one liner that does 90% of the work
#list comprehension to flex
all_tweets = [api.user_timeline(screen_name=user_handle, count=2,lang='en',tweet_mode='extended') for user_handle in fintwit_users]

#uses regex to identify tweets containing a stock ticker
pattern = "\$[a-zA-Z+]"
cashtag_tweets = []

for tweet_list in all_tweets:
  for tweet in tweet_list:
    text = tweet._json["full_text"]
    if re.findall(pattern,text):
      cashtag_tweets.append(text)


# Building a stock dictionary
cashtag_dict = {}

#for tweet in posts[:100]:
for tweet in cashtag_tweets:
  #text = tweet._json["full_text"]
  #breaks up strings into words
  splits = tweet.split()

  for word in splits:
    #if pattern is found in a word
    if re.findall(pattern,word):
      #strip erroneous chars, and keeps $. Do I really need it?
      #word = word.strip(",.?!'[]@()*")
      #Completely cleans all tickers, but removes $. Probably better
      word = re.sub(r'[^a-zA-Z0-9]', '', word)
      if word in cashtag_dict:
        cashtag_dict[word] += 1
      else:
        cashtag_dict[word] = 1
#print(cashtag_dict)

#Init a dataframe and populate with symbol and frequency
tweet_df = pd.DataFrame(cashtag_dict.items(),columns=['Symbol','Frequency'])

#sorted_df
descending_df = tweet_df.sort_values(by=['Frequency'],ascending=False)
#print(descending_df.to_string(index=False))

#printing top 5 from sorted df
#print(descending_df[0:5].to_string(index=False))

#create top 5 dataframe
top_df = descending_df[0:10]