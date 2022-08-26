import tweepy

class MyStreamListener(tweepy.Stream):
    def on_status(self, status):
        print(status.text)  # prints every tweet received

    def on_status(self, status):
        print(status.text)

    def on_error(self, status_code):
        if status_code == 420:  # end of monthly limit rate (500k)
            return False



consumer_key = "hahbSWwAK62nqgdmuESNAvNhA"
consumer_secret = "R3YvB715WGlxOx5zVOQRpC7bwO38w0H6PYyjkYy3T9ZNKNEtcn"
access_token = "1488374561951391746-IpjthOzIQsIDovQluWk2SBzpR6RWqF"
access_token_secret = "FVyrKXiXYLAeBwTDCtYQvQlmJoXeKTDHIwWh3F08DQi88"


#Tokens de api disponibles
#consumer_key = ""
#consumer_secret = ""
#access_token = ""
#access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


stream = TweetsListener()
streamingApi = tweepy.Stream(auth=api.auth, listener=stream)
streamingApi.filter(
    # follow=["151179935"] #Por usuario en especifico,
    track=["virus"] #Por hashtag,
    #locations=[-99.36492421,19.04823668,-98.94030286,19.59275713] # Ciudad de Guatemala
)