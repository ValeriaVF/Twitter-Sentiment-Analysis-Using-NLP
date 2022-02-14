# Sentiment Analysis of Tweets by Brand
#### Authors: Eddie Prado, Sally Heinzel, Valeria Viscarra Fossati, and Weston Shuken

![Header Image](sentiment_analysis_header.png)

######Image by SurveySensum

## Overview
Understanding brand and product reputation is difficult when only provided customer survey and review data. However, there is an abundance of social media responses to products and brands on various platforms. With these unoffical reviews and preferences towards products via tweets from Twitter, we can derive an overall sentiment towards your brand and products.

We are CONSULTING TEAM NAME that can provide you with our state-of-the-art machine learning model that can rate the sentiment of tweets based on users who tweet about your brand. We can provide you with a real-time graph showing the trends of user sentiment towards your brand and products.

## Business Issue
Companies have little insight into their overall brand reputation on social media platforms. Our team of experts can prodivde real-time, accurate analysis of brand reputaiton based on the sentiment analysis of tweets on Twitter.

## Data & Methods
The dataset comes from Crowdflower via [data.world](https://data.world/crowdflower/brands-and-product-emotions) *Created: August 30, 2013 by Kent Cavender-Bares*. The data contains over 9,000 tweets from Twitter users on how they evaluated multiple brands and products. The crowd was asked if the tweet expressed positive, negative, or no emotion towards a brand and/or product. If some emotion was expressed they were also asked to say which brand or product was the target of that emotion. 

We used a binary classifier to predict if a tweet would have a negative or not. We chose to use this binary classification because negative sentiment is much more insightful to a brand versus neutral or positive sentiment. An example of usage could be to monitor if the negative sentiment increases on a particular day, then we can use inferential analysis to find specific tweets that were affecting the rating.


## Results & Evaluation

## Online Application

## Business Proposal Summary

## Next steps

---

#### For more information
Please contact the contributors to this analysis: 
[Eddie Prado]() |
[Sally Heinzel]() |
[Valeria Fossati]() |
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
