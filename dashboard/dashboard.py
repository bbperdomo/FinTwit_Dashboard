#imports the important stuff
from backend import *
from st_styles import *
import streamlit as st


st.sidebar.write("Options")
option = st.sidebar.selectbox("Chose a dashboard", ('FinTwit Pulse','Statistics','Sentiment'))


if option == 'FinTwit Pulse':

    st.markdown('<p class="big-font">FinTwit Pulse - Dashboard</p>', unsafe_allow_html=True)
    st.header("Here are the most mentioned stocks among growth financial twitter users recently:")
    st.subheader("Top 10 stocks")
    st.dataframe(top_df)