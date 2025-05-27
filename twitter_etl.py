import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs

access_key = "HVmnUir0811FKota5NiRJFz6L"
access_secret = "sIoGc0Ax3vbJwdYNluat19524SHllBj1LIYIiirEFIP3kDMr45"
consumer_key = "1905758299389153280-cPRQ3hrFLDcVZb99xVxNFyYfgVOGpr"
consumer_secret = "qU4tWlvGUKnIan3CGGosl2pGET787CF6y10Ac1Dyr2U9l"

BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAAL%2B0AEAAAAAxIAj1%2BB0fHiPMoTDedSWO9cUWvg%3DsE7W9gGTKm177jQd58x7lEKrWWGqRkWFuzn0lpfvzNypHDFFul"

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


