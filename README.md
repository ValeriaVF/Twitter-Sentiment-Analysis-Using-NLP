# Sentiment Analysis of Tweets by Brand
#### Authors: Eddie Prado, Sally Heinzel, Valeria Viscarra Fossati, and Weston Shuken

![Header Image](/images/sentiment_analysis_header.png)

###### Image by SurveySensum

## Overview
Understanding brand and product reputation is difficult when only provided customer survey and review data. However, there is an abundance of social media responses to products and brands on various platforms. With these unoffical reviews and preferences towards products via tweets from Twitter, we can derive an overall sentiment towards your brand and products.

We are VIAGogo that can provide you with our state-of-the-art machine learning model that can rate the sentiment of tweets based on users who tweet about your brand. We can provide you with a real-time graph showing the trends of user sentiment towards your brand and products.

## Business Issue

Companies have little insight into their overall brand reputation on social media platforms. Twitter has the ability to prodivde real-time, accurate analysis of brand reputaiton based on the sentiment analysis of tweets on Twitter. The word cloud below is an example of of how Twitter users are talking about Google and Apple:

<img width="965" alt="Wordcloud" src="https://user-images.githubusercontent.com/79488205/154538264-a0b97af9-dbae-4081-a2e6-bac438df0994.png">

Our team of experts has built a Machine Learning model that uses Natural Language Processing to distinguish between positive and negative sentiment in Tweets. Using Google and Apple mentions on Twitter, we were able to classify sentiment to an 89% accuracy. 

This model will be used as an analytics tool for companies to access their products' popularity on Twitter without having to access Twitter API. 

## Data & Methods
The dataset comes from Crowdflower via [data.world](https://data.world/crowdflower/brands-and-product-emotions) *Created: August 30, 2013 by Kent Cavender-Bares*. The data contains over 9,000 tweets from Twitter users that evaluated multiple brands and products. The crowd was asked if the tweet expressed positive, negative, or no emotion towards a brand and/or product. If some emotion was expressed they were also asked to say which brand or product was the target of that emotion. 

During our exploratory data aalysis, we found that the data was not balanced, as shown by the graphs below: 

![Sentiment Dashboard](https://user-images.githubusercontent.com/79488205/154533171-abf7f63c-6498-4082-9c98-16b1618f05e7.png)


In order to adress this inbalnce, we first used a binary classifier to predict if a tweet would have a negative or not negative response. We chose to use this binary classification because negative sentiment is much more insightful to a brand versus neutral or positive sentiment. An example of usage could be to monitor if the negative sentiment increases on a particular day, then we can use inferential analysis to find specific tweets that were affecting the rating.

## Results & Evaluation

Our baseline binary models classified tweets with an accuracy of 83 - 88%:

<img width="515" alt="Baseline Binary Models" src="https://user-images.githubusercontent.com/79488205/154533341-9aa712da-ded6-4b76-b809-75abea25f450.png">

Once we had this baseline, we continued to tune the models until we reached an accuracy score of 89% with our SGD Classifier model: 

<img width="504" alt="Tuned Binary Models" src="https://user-images.githubusercontent.com/79488205/154537919-16955719-995f-44bd-be1e-7ac72e7c70af.png">


## Online Application

## Business Proposal Summary
Being competitive in the 21st century means utilizing 21st-century tools. ViaGogo’s Twitter Sentiment Analysis, built using natural language processing, offers Twitter an opportunity to give their brand users an advantage in the marketplace. This product enables businesses to capture public reactions about their company and products in a far more timely and authentic manner than focus groups or surveys. It collects and analyzes real-time reactions in order for businesses to make effective decisions.

The Twitter Sentiment Analysis adds value to businesses in 3 main ways:
-	Brand Perception – track what people are saying about a company/product in real-time within a mercurial social media environment;
-	Market Research – identify and explore the sentiments directed at one’s competitors in order to develop strategies based on their successes and struggles;
-	Customer Service – pinpoint which brands, locations, or services are thriving in customer satisfaction and which ones need the most urgent attention.

By adopting Via Gogo’s Twitter Sentiment Analysis and offering it as a service for corporate users, Twitter will increase its utility and make itself an indispensable part of the modern business landscape.

## Next Steps
Via Gogo in currently working on some new applications for its Twitter Sentiment Analysis. One product in development is the Positivity Rater. This tool gives users a positivity rating based on the analysis of the account’s past tweets. This can be useful to increase engagement among Twitters users. With so many people turned off by negative and harmful content, the Positivity Rater allows an individual to gauge how positive someone is when considering whether or not to follow them. We believe this will boost user activity and retain those who otherwise may stop using Twitter due to so much unwanted, pernicious content.

Another area Via GoGo is actively working on is the creation of dashboards, which allow users to easily visualize sentiment analysis both in real-time and longitudinally. These dashboards will filter data on different dimensions, such as time frame, location, and product/service. It will also facilitate easy comparison of a given metric (for example, comparing the sentiments expressed towards 2 different branches or how sentiment about a product compares to this time last year).

Finally, ViaGoGo is already in production of a web app that allows users to write a tweet and see its sentiment rating before publishing it. This will ensure that the author strikes the appropriate tone with their tweet and can prevent thoughtless or poorly constructed tweets from entering the public domain. This feature will be valued by social media managers sitewide.

---

#### For more information
Please contact the contributors to this analysis: 
[Eddie Prado]() |
[Sally Heinzel]() |
[Valeria Viscarra Fossati](https://www.linkedin.com/in/valeria-vf/) |
[Weston Shuken](https://www.linkedin.com/in/westonshuken/)


**Repository Structure:**
```
├── data preprocessing                     <- Team Member's individual notebooks 
├── data                                   <- Both sourced externally and generated from code 
├── images                                 <- Both sourced externally and generated from code 
├── .gitignore                             <- gitignore      
├── README.md                              <- The top-level README for reviewers of this project
├── index.ipynb                            <- Narrative documentation of analysis and modeling
└── presentation.pdf                       <- PDF version of project presentation
```
