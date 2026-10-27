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

# Actualizar datos
updateAlumno = "UPDATE alumnos SET nombre = %s, edad = %s, email = %s WHERE matricula = %s"
valores = ("Alan Turing", 26, "alan@gmail.com", 5)
cursor.execute(updateAlumno, valores)

conexion.commit()

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