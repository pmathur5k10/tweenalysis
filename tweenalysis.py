#chcp 65001
#run this in command promp before running the script to get UTF-8 encoding

import tweepy
#imposrt the twitter library for python scrapping
from textblob import TextBlob 
# A natural learning processing library dependent on nltk and providing direct functions


consumer_key='hwhSZuZZPYjdwY2aRc7eH9MUj'
consumer_secret='dOvqTQ4qflnDiXwD21pyVN3R08KljY5aQdUNmqPp4P0xkfRBSJ'

access_token='100533373-ORJKKM4jfi5BPDXAl9uw5FRjQ3OP3vU8flcN2hFu'
access_token_secret='ytxoocuEwnkMxdfbPBTNfMB9bRUQzb0fX8DLSN8dj377l'
# Consumer and access credentials from twitter developers for access grant

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)
#authorisation of twitter credentials
#api authorisation


query=input("enter the query to be analysed....")
#input query to be searched


public_tweet=api.search(query)
#search for public tweets for query


for t in public_tweet:
	print(t.text)
	analysis=TextBlob(t.text)
	print(analysis.sentiment)
#loop for printing each tweet
#feeding the tweete text to textblob for processing in bag of words
#printing the sentiment of each tweet
