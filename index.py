"""
Este módulo establece una conexión a una base de datos MongoDB y 
realiza una consulta a una colección de pokémon.
"""

import pymongo

MONGO_HOST = "localhost"
MONGO_PORT = "27017"
MONGO_TIMEOUT = 1000

MONGO_URI = "mongodb://" + MONGO_HOST + ":" + MONGO_PORT + "/"

MONGO_DATABASE = "pokemones"
MONGO_COLLECTION = "pokemon"

try:
    client = pymongo.MongoClient(MONGO_URI, serverSelectionTimeoutMS=MONGO_TIMEOUT)
    baseDatos = client[MONGO_DATABASE]
    coleccion = baseDatos[MONGO_COLLECTION]
    for documento in coleccion.find():
        print(documento["nombre"])
    client.close()
except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    print("Tiempo exedido ", errorTiempo)
except pymongo.errors.ConnectionFailure as errorConexion:
    print("Error de conexión ", errorConexion)
