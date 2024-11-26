import sqlite3
from datetime import datetime
from contextlib import contextmanager

class GestorBD:
    def __init__(bd, nombre_bd="notas.db"):
        bd.nombre_bd = nombre_bd
        bd.init_bd()
    #Añadidos para mejorar la gestión de la conexión y evitar ResorceWarning
        bd.conexion = None

    def __enter__(bd):
        bd.conexion = sqlite3.connect(bd.nombre_bd)
        return bd

    def __exit__(bd, exc_type, exc_val, exc_tb):
        if bd.conexion:
            bd.conexion.close()

    # Inicializa la base de datos leyendo el esquema desde un archivo SQL
    def init_bd(bd):
        # Lee el archivo schema.sql que tiene la estructura de la base de datos
        with open('basedatos/schema.sql', 'r') as archivo_schema:
            schema = archivo_schema.read()
        # Crea las tablas en la base de datos
        with sqlite3.connect(bd.nombre_bd) as conexion:
            cursor = conexion.cursor()
            cursor.executescript(schema)

    # Crea una nueva nota en la base de datos
    def crear_nota(nota, titulo, descripcion):
        # Obtiene la fecha y hora actual
        fecha_actual = datetime.now().strftime("%d-%m-%Y %H:%M")
        # Conecta a la base de datos y guarda la nota
        with sqlite3.connect(nota.nombre_bd) as conexion:
            cursor = conexion.cursor()
            cursor.execute('''
                INSERT INTO notas (titulo, descripcion, fecha_creacion, ultima_modificacion)
                VALUES (?, ?, ?, ?)
            ''', (titulo, descripcion, fecha_actual, fecha_actual))
            conexion.commit()
            return cursor.lastrowid  # Devuelve el ID de la nota creada

    # Obtiene todas las notas de la base de datos
    def leer_notas(db):
        with sqlite3.connect(db.nombre_bd) as conexion:
            cursor = conexion.cursor()
            cursor.execute('SELECT * FROM notas')
            notas = cursor.fetchall()
            # Convierte cada nota a un diccionario para que sea más fácil de usar
            return [
                {
                    "id": nota[0],
                    "titulo": nota[1],
                    "descripcion": nota[2],
                    "fecha_creacion": nota[3],
                    "ultima_modificacion": nota[4]
                }
                for nota in notas
            ]

    # Busca y devuelve una nota específica por su ID
    def leer_nota(db, id_nota):
        with sqlite3.connect(db.nombre_bd) as conexion:
            cursor = conexion.cursor()
            cursor.execute('SELECT * FROM notas WHERE id = ?', (id_nota,))
            nota = cursor.fetchone()
            # Si encuentra la nota, la devuelve como diccionario
            if nota:
                return {
                    "id": nota[0],
                    "titulo": nota[1],
                    "descripcion": nota[2],
                    "fecha_creacion": nota[3],
                    "ultima_modificacion": nota[4]
                }
            return None

    # Modifica una nota existente
    def actualizar_nota(db, id_nota, titulo, descripcion):
        fecha_actual = datetime.now().strftime("%d-%m-%Y %H:%M")
        with sqlite3.connect(db.nombre_bd) as conexion:
            cursor = conexion.cursor()
            cursor.execute('''
                UPDATE notas 
                SET titulo = ?, 
                    descripcion = ?, 
                    ultima_modificacion = ?
                WHERE id = ?
            ''', (titulo, descripcion, fecha_actual, id_nota))
            conexion.commit()
            # Devuelve True si se actualizó alguna nota, False si no
            return cursor.rowcount > 0

    # Elimina una nota por su ID
    def eliminar_nota(db, id_nota):
        with sqlite3.connect(db.nombre_bd) as conexion:
            cursor = conexion.cursor()
            cursor.execute('DELETE FROM notas WHERE id = ?', (id_nota,))
            conexion.commit()
            # Devuelve True si se eliminó la nota, False si no existía
            return cursor.rowcount > 0