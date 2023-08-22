# Proyecto de Extracción y Análisis de Tweets

Este proyecto consiste en una serie de scripts en Python que permiten extraer tweets relacionados con un tema específico desde la API de Twitter, almacenarlos en una base de datos MongoDB y luego mostrar y analizar los datos a través de una interfaz gráfica de usuario.

## Componentes

### `extraer_tweets.py`

Este script utiliza la biblioteca Tweepy para autenticarse en la API de Twitter, realizar una consulta de búsqueda y extraer tweets relacionados con el tema especificado en la variable **search_keyword** . Luego, guarda estos datos en un archivo CSV llamado "BigData.csv". Los campos extraídos incluyen ID del tweet, texto, contador de retweets, contador de favoritos, fuente, fecha de creación, ID y nombre del usuario, ubicación y más.

    #Puedes sustituir la palbra clave de busqueda en la siguiente linea:
    search_keyword = "Guatemala"

### `insertarMongoDB.py`

Este script se encarga de leer los datos del archivo CSV "BigData.csv" y los inserta en una base de datos MongoDB. Utiliza la biblioteca pymongo para realizar la inserción de documentos en la colección que se especifica en conexion.py. Los datos extraídos, como el texto del tweet, la fecha de creación, el nombre del usuario y otros, se estructuran en documentos y se insertan en la base de datos.

### `conexion.py`

Este archivo proporciona una función `ObtenerConexion()` que establece una conexión a la base de datos MongoDB. Define la dirección del servidor, el puerto y la URI de conexión. La función obtiene una colección de la base de datos , la cual se utiliza para insertar los documentos.

### `MostrarDatos.py`

Este script crea una interfaz gráfica de usuario (GUI) utilizando la biblioteca Tkinter. Muestra los datos de los tweets almacenados en la base de datos MongoDB en una tabla, y también presenta información sobre las ubicaciones y fuentes más comunes en los datos. El script llama a las funciones definidas en los otros archivos para obtener y mostrar los datos en la GUI.
![Captura de pantalla 1](/img/c1.png)

## Uso

#### 1. Clona este repositorio en tu máquina local:

   
    git clone https://github.com/Jos-mlp/ProyectoTwitter.git
    cd ProyectoTwitter
  
#### 2. Instala las dependencias necesarias:  

     pip install -r requirements.txt
   
#### 3. Configura las credenciales en credentials.py 
        API_KEY = ''
        API_SECRET_KEY = ''
        ACCESS_TOKEN = ''
        ACCESS_TOKEN_SECRET = ''
        
#### 4. Configura la conexion a la base de datos MongoDB en conexion.py
		MONGO_HOST="localhost"  # Dirección del servidor MongoDB

		MONGO_PUERTO="27017"  # Puerto del servidor MongoDB

		MONGO_BASEDATOS="  "  # Nombre de la base de datos

		MONGO_COLECCION="  "  # Nombre de la colección
#### 5. Ejecuta los scripts:

        py extraer_tweets.py
        py insertarMongoDB.py 
        py MostrarDatos.py
    
## Requisitos
-   Python 3
-   MongoDB


## Licencia
    MIT

