from mongodb import Mongo
mongo = Mongo()
diccionario = {
    "llave": "contenido"
}
mongo.insert(diccionario)