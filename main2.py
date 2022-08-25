from tweepy import Stream
import tweepy

class MyStreamListener(Stream):
    def on_status(self, status):
        print(status.text)  # prints every tweet received

    def on_error(self, status_code):
        if status_code == 420:  # end of monthly limit rate (500k)
            return False


consumer_key = "FGqkOJU3o3Rh15alV5Ql4obUX"
consumer_secret = "2vIiKctsxxezL6kKGo4qtyFPDcY1viFz6M1a2bHLTwWrijVXE5"
access_token = "151179935-HLh8FmhbS0D3892npnkfiM6UNc1hLZ0NRHKhZCzJ"
access_token_secret = "tiKTQPpveXHZRsEm0ODUeCJGmlSBqqeUzO7F7cRYKrTp6"

stream = MyStreamListener(consumer_key,
                          consumer_secret,
                          access_token,
                          access_token_secret)

stream.filter(track=["Python"], languages=["en"])