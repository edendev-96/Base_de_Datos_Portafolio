import pymysql

# 1. Configuración de conexión (una sola vez)
datos_conexion = {
    'host': 'localhost',
    'user': 'root',
    'password': 'eden096chr',
    'database': 'MiUniversidad'
}

try:
    # 2. Abrimos la conexión
    conexion = pymysql.connect(**datos_conexion)
    print(" ¡Conexión Exitosa!")
except Exception as e:
    print(f"Ocurrió un error: {e}")

"""
# Insertar nuevos datos
alumnoNuevo = 'INSERT INTO alumnos (nombre, edad, email) VALUES ("Napoleon Bonaparte", 36, "napoleon@email.com")'
cursor.execute(alumnoNuevo)

#Guardar cambios
conexion.commit()

eliminarAlumno = "DELETE FROM alumnos WHERE matricula = 45"
cursor.execute(eliminarAlumno)
"""