import pymongo
import give_me_tweets

class Mongo:
    def __init__(self):
        self.client = pymongo.MongoClient(
            "mongodb+srv://admin:Mayonesa123@cluster0.baxfkya.mongodb.net/?retryWrites=true&w=majority")
        self.db = self.client.apitwitter
        self.collection = self.db.datos

    def insert(self, dato):
        dato_id = self.collection.insert_one(dato).inserted_id
        return dato_id

    def insert_T(self, tex):
        tex_tweet_texto = self.collection.insert_one(tex).inserted_tweet_texto
        return tex_tweet_texto

