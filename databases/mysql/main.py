import mysql.connector

# conexion = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="root",
#     database="tienda"
#     )
#
# if conexion.is_connected():
#     print("Conectado a la base de datos")
#
# conexion.close()

# conexion = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="root",
#     database="tienda"
#     )
#
# cursor = conexion.cursor()
#
# cursor.execute("INSERT INTO productos (nombre, precio) VALUES ('Teclado', 20)")
# conexion.commit()
# conexion.close()
#

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="tienda"
    )

cursor = conexion.cursor()
cursor.execute("SELECT * FROM productos")

for fila in cursor.fetchall():
    print(fila)
conexion.close()
