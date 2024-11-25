#Librería para gestionar fechas con facilidad
from datetime import datetime

class GestorBD:
    def __init__(bd):
        #Simulamos una base de datos con un diccionario
        bd.notas = {}
        bd.id_actual = 0
    
    #Función para crear una nota
    def crear_nota(nota, titulo, descripcion):
        fecha_actual = datetime.now().strftime("%d-%m-%Y %H:%M")
        #Incrementamos el id_actual y lo asignamos a la nota (asignaremos a la primera nota el id 1, que es más intuitivo para el usuario)
        nota.id_actual += 1 
        nota.notas[nota.id_actual] = {
            "titulo": titulo,
            "descripcion": descripcion,
            "fecha_creacion": fecha_actual,
            "ultima_modificacion": fecha_actual
            }
        return nota.id_actual

    #Función para leer todas las notas
    def leer_notas(db):
        return list(db.notas.values())

    #Función para leer una nota en concreto por id
    def leer_nota(db, id_nota):
        return db.notas.get(id_nota)

    #Función para actualizar una nota por id
    def actualizar_nota(db, id_nota, titulo, descripcion):
        nota = db.notas.get(id_nota)
        #Si la nota existe, actualizamos sus datos y devolvemos True
        if nota:
            nota["titulo"] = titulo
            nota["descripcion"] = descripcion
            nota["ultima_modificacion"] = datetime.now().strftime("%d-%m-%Y %H:%M")
            return True
        #Si no existe, devolvemos False
        return False

    #Función para eliminar una nota por id
    def eliminar_nota(db, id_nota):
        #pop elimina la nota si existe el id, y devuelve la nota eliminada, si no existe devuelve None
        nota_eliminada = db.notas.pop(id_nota, None)
        #Si la nota eliminada no es None, devolvemos True, si es None devolvemos False
        eliminada = nota_eliminada is not None
        return eliminada

