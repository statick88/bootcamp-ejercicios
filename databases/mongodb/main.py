from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')

db = client['tienda']

print("Conectado a la base de datos")

coleccion = db['productos']

# producto = {"nombre": "Monitor", "precio": 299.99}
# coleccion.insert_one(producto)
# print("Producto insertado", producto)

# print("Productos en la coleccion")
# for producto in coleccion.find():
#     print(producto)

# coleccion.update_one({"nombre": "Monitor"}, {"$set": {"precio": 199.99}})
# print("Producto actualizado")

coleccion.delete_one({"nombre": "Monitor"})
print(f"Producto eliminado")

print("Productos despues de la eliminacion")
for producto in coleccion.find():
    print(producto)

client.close()
