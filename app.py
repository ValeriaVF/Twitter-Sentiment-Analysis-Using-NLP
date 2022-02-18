from sklearn.metrics import plot_confusion_matrix
import streamlit as st
import pickle


st.title("Tweet Sentiment Analysis")

load_clf = pickle.load(open('final_clf.pkl', 'rb'))

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

st.sidebar.header('We are VIA GoGo')
st.sidebar.image('Select one:', [1, 2])
# st.title("Today's score for Google (example)")
# st.write("See the sentiment from a sample of tweets metioned to Google today")

# show_today = st.button('GoGo!')

# if show_today is True:
#     """Show a table of the scores per tweet and then a ratio of tweets"""


