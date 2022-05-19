from pprint import pp
from pymongo import MongoClient
from bson.objectid import ObjectId
client = MongoClient("mongodb+srv://clase-delfos:AnaliticaDelfos2022@delfosmasterclass.hgs5l.mongodb.net/?retryWrites=true&w=majority")
db = client.masterclass

# print(db)

########## Insersión de un documento


# result = db.personajes.insert_one(
#     {
#         "nombre": "Shrek",
#         "edad": 30,
#         "residencia": "Pantano",
#         "especie": "Ogro",
#         "peliculas": ["Sherk 1", "Sherk 2", "Shrek tercero", "Shrek para siempre"],
#         "hijos": [
#             {"nombre": "Fergus", "genero": "ogro"},
#             {"nombre": "Farkle", "genero": "ogro"},
#             {"nombre": "Felicia", "genero": "ogra"},
#         ]
#     }
# )

# pp(result.inserted_id)

########## Lectura de un documento

# personajes = db.personajes.find()
# for personaje in personajes:
#     pp(personaje)

# personaje = db.personajes.find_one()
# pp(personaje)

########## Insertar dos o mas

# result = db.personajes.insert_many(
#     [
#         {
#             "nombre": "Gato con botas",
#             "edad": 8,
#             "especie": "Gato",
#             "residencia": "Desconocida",
#             "peliculas": ["Sherk2", "Shrek tercero", "Shrek para siempre"]
#         },
#         {
#             "nombre": "Fiona",
#             "edad": 30,
#             "especie": "Ogro",
#             "residencia": "Muy muy lejano",
#             "peliculas": ["Sherk 1", "Sherk2", "Shrek tercero", "Shrek para siempre"],
#             "hijos": [
#                 {"nombre": "Fergus", "genero": "ogro"},
#                 {"nombre": "Farkle", "genero": "ogro"},
#                 {"nombre": "Felicia", "genero": "ogra"},
#             ]
#         },
#         {
#             "nombre": "Encantador",
#             "edad": 32,
#             "especie": "Humano",
#             "residencia": "Desconocida",
#             "peliculas": ["Sherk2", "Shrek tercero"]
#         },
#     ]
# )

# pp(result.inserted_ids)

###### Leer varios

# result = db.personajes.find({"nombre": "Shrek"})
# for r in result:
#     pp(r)

########## Leer Uno
# result = db.personajes.find_one({"_id": ObjectId('62858233ced180d363071095')})
# pp(result)

########## Traernos campos específicos
# doc = db.personajes.find_one({"_id": ObjectId('62858233ced180d363071095')}, {"hijos": 1})
# pp(doc)

####### Actualizar

# result = db.personajes.update_one({"_id": ObjectId('62858233ced180d363071095')}, {"$set": {"residencia": "Muy muy lejano"}})
# pp(result.raw_result)

# result = db.personajes.find_one({"_id": ObjectId('62858233ced180d363071095')})
# pp(result)

####### Eliminar 
# result = db.personajes.delete_one({"nombre": "Encantador"})
# pp(result.deleted_count)

#### Todos

result = db.personajes.delete_many({})
pp(result.deleted_count)