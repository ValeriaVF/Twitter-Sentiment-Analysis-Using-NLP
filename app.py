import streamlit as st
import pickle
import pandas as pd
import numpy as np


st.title("Tweet Sentiment Analysis")

load_clf = pickle.load(open('./model/final_clf.pkl', 'rb'))

tweet_input = st.text_input('Write a Tweet')

show_sentiment = st.button('GoGo!')

def prediction(tweeeeeet):
    pred = str(load_clf.predict([tweeeeeet]))
    return pred

if show_sentiment is True:
    sentiment = prediction(tweet_input)
    # st.text(sentiment)
    # st.text(type(sentiment))
    if sentiment == '[1]':
        st.markdown('##### This tweet is positive')
        st.image('images/happy_gogo.png', width=200)
    elif sentiment == '[0]':
        st.markdown('##### This tweet is neutral')
        st.image('images/neutral_gogo.png', width=200)
    else:
        st.markdown('##### This tweet is negative')
        st.image('images/cry_gogo.png', width=200)
else:
    st.markdown('##### *i am waiting......*')
    st.image('images/shiba_gif_200.gif')

# st.sidebar.header('We are VIA GoGo')


