﻿# ElectivoBD
        Instrucciones

        Requisitos:
    1.- Tener instalado python en una version superior a 3.0
    2.- Tener habilitado el pip cuando se instale python
    3.- Tener instalado pymongo Comando: pip install pymongo

        Pasos para ejecutar:
    1.- Descargar codigo
    2.- Instalar dependencia pip,  
            Comando: pip install pymongo            
    3.- Ejecutar comando: python main.py

        Ambiente virtual
    -env python

        Usos
    Este programa tiene el fin de probar Bases de datos no relacionales, en este caso utilizando la libreria "mongod"

        Base de datos
    En esta base de datos se guarda la infomacion de pokemons.
    A continuación el esquema de la Base de datos:
    Pokemon: Pikachu
    Sexo: Masculino
    Tipo: Electrico
    Nivel: 56

        Archivos que se utilizan
    main.py: Es el codigo donde se ejecuta el programa principal.
    index.py: Es el codigo para establecer la conexión con la base de datos.
    pokemones.pokemon.json: collection que se debe importar.
