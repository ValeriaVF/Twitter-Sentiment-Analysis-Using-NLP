from unicodedata import name
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, plot_confusion_matrix
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import re

class VIA_GoGo:

    """
    A class to clean and tokenize our twitter data for nlp
    processing
    
    ...

    Methods
    -------
    token_tweet_lemmatizer(text, tokenizer, stopwords)
        Converts a string into a list of tokens using
        lemmatizer as a stemmer

    token_tweet_porter(text, tokenizer, stopwords)
        Converts a string into a list of tokens using
        Porter as a stemmer

    clean_tokenizer(dataframe, tokenizer, stopwords, stem='lemmatizer')
        Takes in our twitter data, changes the column names,
        adds and fills the 'brand' column, creates a numerical
        'emotion' column, and fills and creates 'tweet_text_tokenized' 
        'joined_tokens' for nlp processing

    """
    # methods
    def token_tweet_lemmatizer(self, text, tokenizer, stopwords):
        """
        Takes in a sting, RegexpTokenizer instance, and stopwords
        to tokenize and lemmatize a string

        Parameters
        ----------
            text: str
                string to be tokenized and lemmatized
            tokenizer: nltk.tokenize.regexp.RegexpTokenizer
                instanced RegexpTokenizer to use for tokenizing
            stopwords: list
                list of frequent words to have removed from text.

        Returns
        -------
        Tokenized and stemmed string.
        """

        # importing stemmer and instancing the object
        from nltk.stem.wordnet import WordNetLemmatizer
        lemmatizer = WordNetLemmatizer()

        # Tokenize using `tokenizer`
        text = tokenizer.tokenize(text)
        
        # Remove stopwords
        text = [token for token in text if token not in stopwords]
        
        # Stem the tokenized text
        text = [lemmatizer.lemmatize(token) for token in text]

        return text

    def token_tweet_porter(self, text, tokenizer, stopwords):
        """
        Takes in a sting, RegexpTokenizer instance, and stopwords
        to tokenize and stem a string

        Parameters
        ----------
            text: str
                string to be tokenized and stemmed
            tokenizer: nltk.tokenize.regexp.RegexpTokenizer
                instanced RegexpTokenizer to use for tokenizing
            stopwords: list
                list of frequent words to have removed from text.
        
        Returns
        -------
        Tokenized and stemmed string.
        """
        # importing stemmer and instancing the object
        from nltk.stem import PorterStemmer
        stemmer = PorterStemmer()

        # Tokenize using `tokenizer`
        text = tokenizer.tokenize(text)
        
        # Remove stopwords
        text = [token for token in text if token not in stopwords]
        
        # Stem the tokenized text
        text = [stemmer.stem(token) for token in text]

        return text

    def clean_tokenizer(self, dataframe, tokenizer, stopwords, stem='lemmatizer'):
        """
        Takes in a twitter dataframe to be cleaned and altered. Creates the 
        following columns:

        'brand' - captures which company the tweet is directed to
        'emotion_num' - converts the 'emotion'column into numerical 
        'tweet_text_tokenized' - tokenized 'tweet_text'
        'joined_tokens' - joins the tokenized 'tweet_text_tokenized' column

        Parameters
        ----------
            dataframe: pandas.DataFrame
                dataframe to be cleaned and altered
            tokenizer: nltk.tokenize.regexp.RegexpTokenizer
                instanced RegexpTokenizer to use for tokenizing
            stopwords: list
                list of frequent words to have removed from text
            stem: str; default='lemmatizer'
                string to decide which type of stemming to use
                default = 'lemmatizer'
                optional = 'porter'
        
        Returns
        -------
        Cleaned, altered, and tokenized dataframe that is ready for nlp processing.
        """
        # copy the dataframe parameter as to not alter the original data
        df = dataframe.copy()
        
        # Renaming columns for simplicity
        df.rename(columns={'emotion_in_tweet_is_directed_at': 'directed_at', 
                    'is_there_an_emotion_directed_at_a_brand_or_product': 'emotion'}, 
                    inplace=True)

        # Creating series off of df. Ease of use
        tweet = df['tweet_text']
        directed = df['directed_at']
        emotion = df['emotion']

        # Create a list to hold labels and add 'emotion_num' feature to create
        # a numerical representation of 'emotion'
        list_emotions = list(emotion.value_counts().index)
        df['emotion_num'] = emotion.replace(list_emotions, [0,1,-1,0])        

        # Create a list of what we want to catagorize as either apple or google
        apple_ = ['iPad', 'Apple', 'iPad or iPhone App', 'iPhone', 'Other Apple product or service']
        google_ = ['Google', 'Other Google product or service', 'Android App', 'Google', 'Android']

        # Then call mask to establish the apple_ list of phrases into the Apple label.
        # Next, call mask on the newly created feature named 'brand' to replace
        # the Google related strings to 'Google'
        df['brand'] = directed.mask(directed.isin(apple_), 'Apple')
        df['brand'] = df['brand'].mask(directed.isin(google_), 'Google')

        # Removing caps from tweets
        df['tweet_text'] = tweet.str.lower()

        # Creating lists to hold keywords.
        apple_keywords = ['ipad', 'iphone', 'apple', 'itunes', 'sxsw']
        google_keywords = ['google', 'android', 'marissa', 'mayer']

        # dropping one null tweet and reseting the index to use enumerate()
        # in a for loop
        df.dropna(subset=['tweet_text'], inplace=True) 
        df.reset_index(drop=True, inplace=True)

        # Creating a for loop to allow us to find out which tweets are 
        # targetting what. Copied 'brand' column to avoid altering a slice
        # and then reassign to the copy to the 'brand' column to capture.
        brand = df['brand'].copy()

        for idx, text in enumerate(df['tweet_text']):
            if  brand[idx] != 'Google' and brand[idx] != 'Apple':
                if any(word in  text for word in google_keywords):
                    brand.iloc[idx] = 'Google'
                elif any(word in  text for word in apple_keywords):
                    brand.iloc[idx] = 'Apple'

        df['brand'] = brand

        # Dropping 3 unrelated/not useful tweets. Reseting index.   
        df.dropna(subset=['brand'], inplace=True)
        df.drop(index=df.index[-1], inplace=True)

        df.reset_index(drop=True, inplace=True)

        # Creating a tokenized tweet_text column using stopwords and a stemmer.
        # This calls the token_tweet_lemmatizer function by default. Otherwise, it calls
        # the token_tweet_porter function when stem parameter equals 'porter'.
        if stem == 'porter':
            df['tweet_text_tokenized'] = df['tweet_text'].apply(lambda x: self.token_tweet_porter(x, tokenizer, stopwords))
        else:
            df['tweet_text_tokenized'] = df['tweet_text'].apply(lambda x: self.token_tweet_lemmatizer(x, tokenizer, stopwords))

        df['joined_tokens'] = df['tweet_text_tokenized'].str.join(" ")

        # Returns a nlp pre-processed dataframe
        return df


    def run_model(self, clf, table, X, y, type_='model', join_str=True, plot_models=False, pipeline=True):
        """
        Takes in a model, metric table, X, y, type of model and whether or not
        the X vairble needs to be joined or not.

        The function splits the X & y in to training and testing sets.
        The model is fit to the trained X and does cross validation.
        The model then predicts and provides accuracy score for the test X.

        The funciton returns a metric table with Model, Mean CV, Accuracy, & Type.


        Parameters
        ----------
            clf: Pipline with vecotirzer and estimator
                pipline with vecotirzer and estimator
            table: DataFrame
                used for appending scores.
            X: pandas.Series.series 
                series of text features
            y: pandas.Series.series
                series of categorical predictors
            type_: str; type of model. e.g. 'baseline'
                appends to table
            join_str: boolean
                if X is tokenized, join_str=True will join the text for vectorization.
                default='True'
        
        Returns
        -------
        Metric table with model scoring.
        """

        if join_str == True:
            X = [' '.join(tweet) for tweet in X]
        else:
            X = X
    
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.25, random_state=5)
        
        clf.fit(X_train, y_train)
        
        cv_score = cross_val_score(clf, X_train, y_train, cv=5)
        cv_score_mean = round(np.mean(cv_score), 4)
    
        y_pred = clf.predict(X_test)
        acc_score = accuracy_score(y_pred, y_test)

        
        if pipeline == True:
            model_name = str(clf[2])
            model_name = re.sub("([\(\[]).*?([\)\]])", "\g<1>\g<2>", model_name)
        elif pipeline != True:
            model_name = str(clf)
            model_name = re.sub("([\(\[]).*?([\)\]])", "\g<1>\g<2>", model_name)

        
        
        table = table.append({'Model': model_name + type_, 'CV Score': cv_score_mean, 'Test Accuracy': round(acc_score, 4), 'Type': type_}, ignore_index=True)


        return table

    def plot_models(self, table):
        sns.set_style('darkgrid')
        sns.set_context('poster')
        fig, ax = plt.subplots(figsize=(20, 10))
        plt.bar(table.Model, table['Test Accuracy']*100, color='lightblue', label='Test Accuracy')
        plt.plot(table.Model, table['CV Score']*100, color='blue', label='CV Score')
        plt.ylim(50, 109)
        plt.grid(False)
        plt.xticks(rotation=40, ha='right') 
        plt.ylabel('Scoring (%)')
        plt.title('Model Improvements')
        plt.legend(loc="upper left")   
        plt.show() 
        return 
