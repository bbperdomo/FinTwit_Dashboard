#imports the important stuff
from backend import *
from st_styles import *
import streamlit as st


st.sidebar.write("Options")
option = st.sidebar.selectbox("Chose a dashboard", ('FinTwit Pulse','Statistics','Sentiment'))


if option == 'FinTwit Pulse':

    st.markdown('<p class="big-font">Hello World !!</p>', unsafe_allow_html=True)
    st.header("Here are the most mentioned stocks among growth financial twitter users")
    st.subheader("FinTwit Pulse")
    st.dataframe(top_df)