from os import write
import streamlit as st
import pandas as pd
import numpy as np
import tweepy
import config

#init tweepy api
auth = tweepy.OAuthHandler(config.TWITTER_CONSUMER_KEY, config.TWITTER_CONSUMER_SECRET)
auth.set_access_token(config.TWITTER_ACCESS_TOKEN, config.TWITTER_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


st.sidebar.write("Options")
option = st.sidebar.selectbox("Chose a dashboard", ('User feed','Statistics','Sentiment'))

st.header(option)

if option == 'User feed':
    st.subheader("This is the twitter dashboard")

    for username in config.ct_users:
        user = api.get_user(username)
        tweets = api.user_timeline(username)
        
        for tweet in tweets:
            if '$' in tweet.text:
                st.write(tweet.text)


