from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import pymongo

MONGO_HOST="localhost"
MONGO_PORT="27017"
MONGO_TIMEOUT=1000

MONGO_URI="mongodb://"+MONGO_HOST+":"+MONGO_PORT+"/"

MONGO_DATABASE="pokemones"
MONGO_COLLECTION="pokemon"

try:
    client=pymongo.MongoClient(MONGO_URI,serverSelectionTimeoutMS=MONGO_TIMEOUT)
    baseDatos=client[MONGO_DATABASE]
    collection=baseDatos[MONGO_COLLECTION]
    for documento in collection.find():
        print(documento["nombre"])
    #client.server_info()
    #print("Conexión exitosa en mongo")
    client.close()
except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    print("Tiempo exedido ",errorTiempo)
except pymongo.errors.ConnectionFailure as errorConexion:
    print("Error de conexión ",errorConexion)
