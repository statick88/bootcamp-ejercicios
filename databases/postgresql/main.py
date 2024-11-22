import psycopg2

# Connect to the database
conexion = psycopg2.connect(
    host="localhost",
    database="tienda",
    user="postgres",
    password="root"
    )

# if conexion:
#     print("Conectado a la base de datos PostgreSQL")

# cursor = conexion.cursor()
#
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS productos (
#     id SERIAL PRIMARY KEY,
#     nombre VARCHAR(255) NOT NULL,
#     precio FLOAT NOT NULL
#     )
# ))""")
# conexion.commit()

# cursor = conexion.cursor()
# cursor.execute("INSERT INTO productos (nombre, precio) VALUES (%s, %s)",('Monitor', 299.99))
# conexion.commit()

# cursor = conexion.cursor()
# cursor.execute("SELECT * FROM productos")
#
# for fila in cursor.fetchall():
#     print(fila)

cursor = conexion.cursor()
cursor.execute("DELETE FROM productos WHERE id = 1")
conexion.commit()

conexion.close()
