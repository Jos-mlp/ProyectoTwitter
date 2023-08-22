import tweepy
import pandas as pd
import credentials

def ExtraerTweets():
    # Autenticación de la API de Twitter
    auth = tweepy.OAuth1UserHandler(
        credentials.API_KEY, credentials.API_SECRET_KEY,
        credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET
    )

    # Creación de la API de Tweepy
    api = tweepy.API(auth, wait_on_rate_limit=True)

    # Define la palabra clave de búsqueda
    search_keyword = "Guatemala"

    # Consulta de búsqueda para tweets relacionados con la palabra clave, excluyendo retweets, respuestas y enlaces
    search_query = f"'{search_keyword}' -filter:retweets AND -filter:replies AND -filter:links"

    no_of_tweets = 100

    try:
        # Intenta obtener tweets relacionados con la búsqueda
        tweets = tweepy.Cursor(api.search_tweets, q=search_query, lang="es", tweet_mode="extended").items(no_of_tweets)
        
        # Lista para almacenar los datos de los tweets
        tweets_data = []
        
        # Recorriendo los tweets y extrayendo datos
        for tweet in tweets:
            tweet_data = {
                "tweetID": tweet.id,
                "tweetText": tweet.full_text,
                "tweetRetweetCt": tweet.retweet_count,
                "tweetFavoriteCt": tweet.favorite_count,
                "tweetSource": tweet.source,
                "tweetCreated": tweet.created_at,
                "userID": tweet.user.id,
                "userScreen": tweet.user.screen_name,
                "userName": tweet.user.name,
                "userCreateDt": tweet.user.created_at,
                "userDesc": tweet.user.description,
                "userFollowerCt": tweet.user.followers_count,
                "userFriendsCt": tweet.user.friends_count,
                "userLocation": tweet.user.location,
                "userTimezone": tweet.user.time_zone,
                "Coordinates": tweet.coordinates,
                "GeoEnabled": tweet.user.geo_enabled,
                "Language": tweet.lang,
                "TweetPlace": tweet.place
            }
            tweets_data.append(tweet_data)
        
        # Creación de un DataFrame
        tweets_df = pd.DataFrame(tweets_data)
        
        # Guardar DataFrame en un archivo CSV
        csv_filename = "BigData.csv"
        tweets_df.to_csv(csv_filename, index=False)
        
        print(f"Datos de los tweets almacenados en {csv_filename}")
        
    except BaseException as e:
        print('Error:', str(e))

ExtraerTweets()