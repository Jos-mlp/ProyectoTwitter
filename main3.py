import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import Stream
import pandas as pd
import json
import csv
import sys
import time

j=0

ckey = "hahbSWwAK62nqgdmuESNAvNhA"
csecret = "R3YvB715WGlxOx5zVOQRpC7bwO38w0H6PYyjkYy3T9ZNKNEtcn"
atoken = "1488374561951391746-IpjthOzIQsIDovQluWk2SBzpR6RWqF"
asecret = "FVyrKXiXYLAeBwTDCtYQvQlmJoXeKTDHIwWh3F08DQi88"

OAUTH_KEYS = {'consumer_key':ckey, 'consumer_secret':csecret, 'access_token_key':atoken, 'access_token_secret':asecret}
auth = tweepy.OAuthHandler(OAUTH_KEYS['consumer_key'], OAUTH_KEYS['consumer_secret'])

api = tweepy.API(auth)
if (not api):
    print ("Can't Authenticate")
    sys.exit(-1)
else:
    print ("Scraping data now") # Enter lat and long and radius in Kms  q='hello'
    cursor = tweepy.Cursor(api.search_tweets, q="Guatemala", result_type="new", geocode="15.783471,-90.230759,1000km",lang='es',count=100)
    results=[]
    for item in cursor.items(1000): # Remove the limit to 1000
        print(item.id)
        print(item.text.encode('utf-8'))
        print(item.user.id)
        print(item.user.name)
        print(item.user.description)

        results.append(item)

def toDataFrame(tweets):
    # COnvert to data frame
    DataSet = pd.DataFrame()

    DataSet['tweetID'] = [tweet.id for tweet in tweets]
    DataSet['tweetText'] = [tweet.text.encode('utf-8') for tweet in tweets]
    DataSet['tweetRetweetCt'] = [tweet.retweet_count for tweet in tweets]
    DataSet['tweetFavoriteCt'] = [tweet.favorite_count for tweet in tweets]
    DataSet['tweetSource'] = [tweet.source for tweet in tweets]
    DataSet['tweetCreated'] = [tweet.created_at for tweet in tweets]
    DataSet['userID'] = [tweet.user.id for tweet in tweets]
    DataSet['userScreen'] = [tweet.user.screen_name for tweet in tweets]
    DataSet['userName'] = [tweet.user.name for tweet in tweets]
    DataSet['userCreateDt'] = [tweet.user.created_at for tweet in tweets]
    DataSet['userDesc'] = [tweet.user.description for tweet in tweets]
    DataSet['userFollowerCt'] = [tweet.user.followers_count for tweet in tweets]
    DataSet['userFriendsCt'] = [tweet.user.friends_count for tweet in tweets]
    DataSet['userLocation'] = [tweet.user.location for tweet in tweets]
    DataSet['userTimezone'] = [tweet.user.time_zone for tweet in tweets]
    DataSet['Coordinates'] = [tweet.coordinates for tweet in tweets]
    DataSet['GeoEnabled'] = [tweet.user.geo_enabled for tweet in tweets]
    DataSet['Language'] = [tweet.user.lang for tweet in tweets]
    tweets_place= []
    #users_retweeted = []
    for tweet in tweets:
        if tweet.place:
            tweets_place.append(tweet.place.full_name)
        else:
            tweets_place.append('null')
    DataSet['TweetPlace'] = [i for i in tweets_place]
    #DataSet['UserWhoRetweeted'] = [i for i in users_retweeted]

    return DataSet

DataSet = toDataFrame(results)
DataSet.to_csv('BigData.csv',index=False)