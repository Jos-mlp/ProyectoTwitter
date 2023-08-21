import csv
import pymongo
from datetime import datetime
import conexion

# Conexión a la base de datos MongoDB
coleccion = conexion.ObtenerConexion()

# Abre el archivo CSV y lee los datos
with open('BigData.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        try:
            # Convierte la fecha y hora a un objeto datetime
            tweet_created = datetime.strptime(row['tweetCreated'], '%Y-%m-%d %H:%M:%S+00:00')

            # Crea un documento para insertar en MongoDB
            tweet_document = {
                'tweetID': int(row['tweetID']),
                'tweetText': row['tweetText'],
                'tweetRetweetCt': int(row['tweetRetweetCt']),
                'tweetFavoriteCt': int(row['tweetFavoriteCt']),
                'tweetSource': row['tweetSource'],
                'tweetCreated': tweet_created,
                'userID': int(row['userID']),
                'userScreen': row['userScreen'],
                'userName': row['userName'],
                'userCreateDt': datetime.strptime(row['userCreateDt'], '%Y-%m-%d %H:%M:%S+00:00'),
                'userDesc': row['userDesc'],
                'userFollowerCt': int(row['userFollowerCt']),
                'userFriendsCt': int(row['userFriendsCt']),
                'userLocation': row['userLocation'],
                'userTimezone': row['userTimezone'],
                # Agrega más campos según sea necesario
            }
            # Inserta el documento en la colección
            coleccion.insert_one(tweet_document)
        except pymongo.errors.ConnectionFailure as error:
            print(error)

print("Datos insertados en MongoDB.")
