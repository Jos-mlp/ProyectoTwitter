import pymongo

def ObtenerConexion():
    """Devuelve la conexion a la base de datos"""
    MONGO_HOST="localhost" # Dirección del servidor MongoDB
    MONGO_PUERTO="27017"  # Puerto del servidor MongoDB
    MONGO_TIEMPO_FUERA=1000 # Tiempo de espera en milisegundos

    MONGO_URI="mongodb://"+MONGO_HOST+":"+MONGO_PUERTO+"/"  # URI de conexión

    MONGO_BASEDATOS="twitter_db" # Nombre de la base de datos
    MONGO_COLECCION="tweets" # Nombre de la colección

    try:
        cliente = pymongo.MongoClient(MONGO_URI, serverSelectionTimeoutMS=MONGO_TIEMPO_FUERA) 
        cliente.server_info()  # Intenta acceder a la información del servidor

        # Accede a la base de datos y la colección
        baseDatos = cliente[MONGO_BASEDATOS]  
        coleccion = baseDatos[MONGO_COLECCION]  
        
        print("Conexión a MongoDB exitosa.")
        
        return coleccion
    
    except pymongo.errors.ServerSelectionTimeoutError:
        print("Error: No se pudo conectar a MongoDB. Verifica la configuración.")
        return None
