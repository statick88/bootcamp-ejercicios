import psycopg2

# try:
#     conexion = psycopg2.connect(
#     host="localhost",
#     database="tienda",
#     user="postgres",
#     password="root"
#     )
#     print("Conexión exitosa")
#     conexion.close()
# except Exception as e:
#     print(f"Ocurrió un error: {e}")
#
# try:
#     conexion = psycopg2.connect(
#     host="localhost",
#     database="tienda",
#     user="postgres",
#     password="root"
#     )
#     cursor = conexion.cursor()
#     print("Conexión exitosa")
#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS productos(
#         id serial PRIMARY KEY,
#         nombre VARCHAR(255) NOT NULL,
#         precio NUMERIC(10, 2) NOT NULL
#     )
#     """)
#     conexion.commit()
#     print("Tabla creada exitosamente")
#     conexion.close()
# except Exception as e:
#     print(f"Ocurrió un error: {e}")

# try:
#     conexion = psycopg2.connect(
#     host="localhost",
#     database="tienda",
#     user="postgres",
#     password="root"
#     )
#     cursor = conexion.cursor()
#     print("Conexión exitosa")
#     cursor.execute("INSERT INTO productos(nombre, precio) VALUES('Teclado', 50.00)")
#     conexion.commit()
#     print("Registro insertado exitosamente")
#     conexion.close()
# except Exception as e:
#     print(f"Ocurrió un error: {e}")

# try:
#     conexion = psycopg2.connect(
#     host="localhost",
#     database="tienda",
#     user="postgres",
#     password="root"
#     )
#     cursor = conexion.cursor()
#     print("Conexión exitosa")
#     cursor.execute("UPDATE productos SET precio = 60.00 WHERE nombre = 'Teclado'")
#     conexion.commit()
#     print("Registro actualizado exitosamente")
#     conexion.close()
# except Exception as e:
#     print(f"Ocurrió un error: {e}")

try:
    conexion = psycopg2.connect(
    host="localhost",
    database="tienda",
    user="postgres",
    password="root"
    )
    cursor = conexion.cursor()
    print("Conexión exitosa")
    cursor.execute("DELETE FROM productos WHERE nombre = 'Teclado'")
    conexion.commit()
    print("Registro eliminado exitosamente")
    conexion.close()
except Exception as e:
    print(f"Ocurrió un error: {e}")
