#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 19:31:19 2019

@author: dhirajpatra
"""
import tweepy
from textblob import TextBlob
import csv

# you have to change the values from your api.tweeter.com or developer.tweeter.com
consumer_key = 'your_key'
consumer_secret = 'your_secret'

access_token = 'your_token'
access_token_secret = 'your_token_secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search(input('Enter the tweeter keyword want to search sentiment analysis for: '))

with open('twitter_sentiment_analysis.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['Tweet', 'Sentiment', 'Subjectivity'])

    for tweet in public_tweets:
        #    print(tweet.text)
        analysis = TextBlob(tweet.text)
        #    print(analysis.sentiment.polarity)
        if analysis.sentiment.polarity < 0:
            sentiments = 'Negative'
        else:
            sentiments = 'Positive'

        if analysis.sentiment.subjectivity > 0.5:
            subj = 'Subjective'
        else:
            subj = 'Objective'

        filewriter.writerow([tweet.text, sentiments, subj])

print('Sentiment analysis csv file created here twitter_sentiment_analysis.csv')
