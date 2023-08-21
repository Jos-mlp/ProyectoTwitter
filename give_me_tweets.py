import tweepy
import pandas as pd
import credentials

# Se pasa la clave de autenticación de la API de Twitter
auth = tweepy.OAuth1UserHandler(
    credentials.API_KEY, credentials.API_SECRET_KEY,
    credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET
)

# Se instancia la API de Tweepy
api = tweepy.API(auth, wait_on_rate_limit=True)

# Consulta de búsqueda para tweets relacionados con guatemala, excluyendo retweets, respuestas y enlaces
search_query = "'ref''guatemala'-filter:retweets AND -filter:replies AND -filter:links"
no_of_tweets = 100

try:
     # Se intenta obtener un número determinado de tweets relacionados con la búsqueda
    tweets = api.search_tweets(q=search_query, lang="es", count=no_of_tweets, tweet_mode ='extended')
    
   # Extracción de algunos atributos de los tweets y almacenamiento en una lista
    attributes_container = [[tweet.user.name, tweet.created_at, tweet.favorite_count, tweet.source, tweet.full_text] for tweet in tweets]

    # Lista de nombres de columnas para renombrar en el DataFrame
    columns = ["User", "Date Created", "Number of Likes", "Source of Tweet", "Tweet"]
    
    # Creación del DataFrame utilizando los datos extraídos
    tweets_df = pd.DataFrame(attributes_container, columns=columns)
except BaseException as e:
    print('Status Failed On,',str(e))