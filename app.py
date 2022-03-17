from turtle import textinput
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

st.sidebar.markdown("# Brought to you by")

st.sidebar.image("images/ViaGoGo_logo.png", width=175)

st.sidebar.markdown("## Background") 
st.sidebar.markdown("Understanding brand and product reputation \
    is difficult when companies only have access to customer surveys and online review data. \
    However, there is an abundance of social media user posts about products and brands from various platforms. \
    With these unofficial reviews and preferences towards products via tweets from **Twitter**, \
    we can derive an overall sentiment towards your brand and products. \
    Our company, ViaGoGo, can provide you with a state-of-the-art machine learning model that rates your products \
    and brand sentiment based tweet towards your company. Test it out by typing a tweet on the right. ---> ") 


#### WORKING ON ADDING AN API PULL OF TWEETS ####

# st.sidebar.markdown("You can also type in your company's Twitter handle below and collexct a \
#     sample of today's tweets with their sentiment scores.")

# handle = st.sidebar.text_input('Twitter Handle', value='@Google')
# generate = st.sidebar.button('Collect Samples')

st.sidebar.markdown("## Data & Methods") 

st.sidebar.markdown("The model was trained on a dataset from Crowdflower via [data.world](https://data.world/crowdflower/brands-and-product-emotions) *Created: August 30, 2013 by Kent Cavender-Bares*")
st.sidebar.markdown("The data contains over 9,000 tweets from Twitter users that evaluated multiple brands and products. \
    The crowd was asked if the tweet expressed positive, negative, or no emotion towards a brand and/or product. \
    If some emotion was expressed, they were also asked to say which brand or product was the target of that emotion.") 
st.sidebar.markdown("#### For more information")

st.sidebar.markdown("Please check out our [Github](https://github.com/westonshuken/Twitter-Sentiment-Analysis)")

#### WILL GENERATE SENTIMENT REPORT FROM API PULL ####
# if generate:



