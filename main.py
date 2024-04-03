from pymongo import MongoClient

# Conexión base de datos
client = MongoClient("mongodb://localhost:27017/")
baseDatos = client['pokemones']
coleccion = baseDatos['pokemon']

#MOSTRAR POKEMONES
def mostrarPokemon():
    for pokemon in coleccion.find():
        print("Nombre:",pokemon["nombre"], "Sexo:",pokemon["sexo"], "Tipo:",pokemon["tipo"], "Nivel:",pokemon["nivel"])

#AÑADIR UN POKEMON
def añadirPokemon():
    nombre = input("Ingrese el nombre del Pokémon: ")
    sexo = input("Ingrese el sexo del Pokémon: ")
    tipo = input("Ingrese el tipo del Pokémon: ")
    nivel = int(input("Ingrese el nivel del Pokémon: "))
    nuevo_pokemon = {
        "nombre": nombre,
        "sexo": sexo,
        "tipo": tipo,
        "nivel": nivel
    }
    coleccion.insert_one(nuevo_pokemon)
    print("Pokémon añadido exitosamente.")

#ACTUALIZAR UN POKEMON
def actualizarPokemon():
    nombre = input("Ingrese el nombre del Pokémon que desea actualizar: ")
    nuevo_nombre = input("Ingrese el nuevo nombre del Pokémon: ")
    nuevo_sexo = input("Ingrese el nuevo sexo del Pokémon: ")
    nuevo_tipo = input("Ingrese el nuevo tipo del Pokémon: ")
    nuevo_nivel = int(input("Ingrese el nuevo nivel del Pokémon: "))
    coleccion.update_one({"nombre": nombre}, {"$set": {"nombre": nuevo_nombre, "sexo": nuevo_sexo, "tipo": nuevo_tipo, "nivel": nuevo_nivel}})
    print("Pokémon actualizado exitosamente.")

#Eliminar un Pokémon
def eliminarPokemon():
    nombre = input("Ingrese el nombre del Pokémon que desea eliminar: ")
    coleccion.delete_one({"nombre": nombre})
    print("Pokémon eliminado exitosamente.")

def mostrarMenu():
    print("1. Consultar todos los Pokémon")
    print("2. Añadir un nuevo Pokémon")
    print("3. Actualizar un Pokémon")
    print("4. Eliminar un Pokémon")
    print("5. Salir")

def main():
    while True:
        mostrarMenu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrarPokemon()
        elif opcion == "2":
            añadirPokemon()
        elif opcion == "3":
            actualizarPokemon()
        elif opcion == "4":
            eliminarPokemon()
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
