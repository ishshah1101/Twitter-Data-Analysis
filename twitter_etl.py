import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs

access_key = ""
access_secret = ""
consumer_key = ""
consumer_secret = ""

BEARER_TOKEN = ""

#Twitter Authentication(connects code and twitterAPI)
auth = tweepy.OAuthHandler(access_key , access_secret)
auth.set_access_token(consumer_key , consumer_secret)

#Creating an API object
api = tweepy.API(auth)

# tweets = api.user_timeline( screen_name='@elonmusk',
#                            count=200,
#                            include_rts = False,
#                            tweet_mode = 'extended')

client = tweepy.Client(bearer_token=BEARER_TOKEN)

query = "from:elonmusk -is:retweet"
tweets = client.search_recent_tweets(query=query, max_results=10)

for tweet in tweets.data:
    print(tweet.text)


