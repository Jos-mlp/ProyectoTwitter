import credentials
import tweepy
import time

# Autenticación e ingreso
auth = tweepy.OAuthHandler(credentials.API_KEY, credentials.API_SECRET_KEY)
auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)


# Probando la conexión
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
    # print(f'{tweet.user.screen_name}:\ntweet.text\n{"*"*60}')


# Obtener los tweets de un topic
id = None
count = 0
while count <= 3000:
    tweets = api.search_tweets(q='#gt', lang='es', tweet_mode='extended', max_id=id)
    for tweet in tweets:
        if tweet.full_text.startswith('RT'):
            count += 1
            continue
        f = open('./prueba.txt', 'a', encoding='utf-8')
        
        tweet_id = tweet.id #Id tweet int
        tweet_texto = tweet.full_text #texto tweet
        tweet_Source = tweet.source #Desde donde tweetean
        tweet_Created = tweet.created_at #Fecha de creacion del usuario
        user_id = tweet.user.id #ID usuario
        user_name = tweet.user.name #Nombre del usuario
        user_Create_Dt = tweet.user.created_at #Fecha de creacion del usuario
        userDesc = tweet.user.description #Descripcion del usuario
        userFollowerCt = tweet.user.followers_count #Personas a las que sigue la cuenta
        userFriendsCt = tweet.user.friends_count #Personas que siguen a la cuenta
        userLocation = tweet.user.location #Ubicacion del usuario

        f.write("Tweet_id: " + str(tweet_id)  + '\n' + "Texto tweet: " +  tweet_texto + '\n'+ "tweet_Source :  " + str(tweet_Source) + '\n'
        + "tweet_Created: " + str(tweet_Created) + '\n' + "user_id: " + str(user_id) + '\n' + "User_Name: " + str(user_name) + '\n'
        + "user_Create_Dt: " + str(user_Create_Dt) + '\n' + "userDesc: " + str(userDesc) + '\n' + "userFollowerCt: " + str(userFollowerCt) + '\n'
        + "userFriendsCt: " + str(userFriendsCt) + '\n' + "userLocation: " + str(userLocation) + '\n' + "userTimezone: " '\n'+ '*'*50 + '\n') # usa esto si quieres tener separados los tweets
        f.close
        count += 1
        id = tweet.id
    print(count)
    print(id)
    time.sleep(1)
