from tweepy import Stream
import tweepy

class MyStreamListener(Stream):
    def on_status(self, status):
        print(status.text)  # prints every tweet received

    def on_error(self, status_code):
        if status_code == 420:  # end of monthly limit rate (500k)
            return False


consumer_key = "hahbSWwAK62nqgdmuESNAvNhA"
consumer_secret = "R3YvB715WGlxOx5zVOQRpC7bwO38w0H6PYyjkYy3T9ZNKNEtcn"
access_token = "1488374561951391746-IpjthOzIQsIDovQluWk2SBzpR6RWqF"
access_token_secret = "FVyrKXiXYLAeBwTDCtYQvQlmJoXeKTDHIwWh3F08DQi88"

stream = MyStreamListener(consumer_key,
                          consumer_secret,
                          access_token,
                          access_token_secret)

stream.filter(track=["Python"], languages=["en"])