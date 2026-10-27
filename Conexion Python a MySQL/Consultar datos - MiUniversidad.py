import mysql.connector

# 1. Conexión a MySQL
conexion = mysql.connector.connect(
host="localhost",
user="root",
password="eden096chr",
database="MiUniversidad"
)

# 2. Cursor
cursor = conexion.cursor()

# Insertar nuevos datos
# alumnoNuevo = 'INSERT INTO alumnos (nombre, edad, email) VALUES ("Napoleon Bonaparte", 36, "napoleon@email.com")'
# cursor.execute(alumnoNuevo)

# conexion.commit()

# 3. Consulta
sql = "SELECT * FROM alumnos"
cursor.execute(sql)

# 4. Obtener datos
resultados = cursor.fetchall()

# 5. Mostrar datos
print("\n--- LISTA DE ESTUDIANTES ---\n")
for fila in resultados:
    print(f"Estudiante: {fila[1]} | Edad: {fila[2]} | Fecha de Registro: {fila[3]} | Email: {fila[4]}")

# 6. Cerrar conexión
conexion.close()