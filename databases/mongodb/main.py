from pymongo import MongoClient

try:
    cliente = MongoClient('localhost', 27017)
    print("Conexión exitosa")
except Exception as e:
    print(f"Error: {e}")

try:
    db = cliente['tienda']
    print("Base de datos tienda seleccionada")
    coleccion = db['productos']
    print("Colección productos seleccionada")
except Exception as e:
    print(f"Error: {e}")

# # Insertar un documento
#
# try:
#     producto = {"nombre": "Laptop", "precio": 15000}
#     resultado = coleccion.insert_one(producto)
#     print(f"Producto insertado con éxito: {resultado.inserted_id}")
# except Exception as exception:
#     print(f"Error: {exception}")
#
# try: 
#     print("Listando productos")
#     for producto in coleccion.find():
#         print(producto)
# except Exception as e:
#     print(f"Error: {e}")
#
# # Actualizar un documento
#
# try:
#     resultado = coleccion.update_one({"nombre": "Laptop"}, {"$set": {"precio": 20000}})
#     print(f"Producto actualizado con éxito: {resultado.modified_count}")
#     if resultado.modified_count > 0:
#         print("Producto actualizado con éxito")
#     else:
#         print("Producto no encontrado")
# except Exception as e:
#     print(f"Error: {e}")
#
# try:
#     print("Listando productos")
#     for producto in coleccion.find():
#         print(producto)
# except Exception as e:
#     print(f"Error: {e}")

# Eliminar un documento

try:
    resultado = coleccion.delete_one({"nombre": "Laptop"})
    print(f"Producto eliminado con éxito: {resultado.deleted_count}")
    if resultado.deleted_count > 0:
        print("Producto eliminado con éxito")
    else:
        print("Producto no encontrado")
except Exception as e:
    print(f"Error: {e}")

try:
    print("Listando productos")
    for producto in coleccion.find():
        print(producto)
except Exception as e:
    print(f"Error: {e}")
