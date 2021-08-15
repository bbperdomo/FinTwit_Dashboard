import streamlit as st
import pandas as pd
import numpy as np


#Displaying text
st.title("This is the title")
st.header("A header")

st.write("some text")

#magic command examples
# """
# # header
# ## sub header
# """

a_dict = {
    "key":"value",
}

some_list = [1,2,3]
st.write(a_dict)
st.write(some_list)

#data frame example
df = pd.DataFrame(
np.random.randn(50, 20),
columns=('col %d' % i for i in range(20)))
st.dataframe(df)  # Same as st.write(df)

#Image example

st.image("https://assets.coingecko.com/coins/images/1/large/bitcoin.png?")

#select box
st.sidebar.write("Options")
option = st.sidebar.selectbox("Chose a dashboard", ('Twitter','Sentiment'))

st.header(option)

if option == 'Twitter':
    st.subheader("This is the twitter dashboard")

if option == 'Sentiment':
    st.subheader("This is the sentiment analysis dashboard")
