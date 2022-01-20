# Financial Twitter Dashboard

This is my stock metrics dashboard hosted on streamlit.

It displays useful information based on what prominent users in the financial twitter, or 'FinTwit' community are talking about currently.
This application allows me to see what stocks seasoned investors are discussing the most at any given time, which is really useful in brainstorming stock pick ideas, or just catching up on financial market news.

I achieved this by using Twitter's api, and a python library called Tweepy, which allowed me to scrape and aggregate twitter users' data. I also incorporated several python libraries to perform data sanitization, and data manipulation:

* I used python's Regular Expression(re) library to strip user's tweets of irrelevant information, isolating only the stock ticker to be processed.
* I implemented a hash table dictionary to dynamically store stock tickers and the number of times they were mentioned overall.
* I used Pandas to store the stocks to more easily calculate important metrics, like which stock was the most mentioned.


