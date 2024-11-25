#Librería para gestionar fechas con facilidad
from datetime import datetime

class GestorBD:
    def __init__(bd):
        #Simulamos una base de datos con un diccionario
        bd.notas = {}
        bd.id_actual = 0
    
def crear_nota(nota, titulo, descripcion):
    fecha_actual = datetime.now().strftime("%d-%m-%Y %H:%M")
    nota.id_actual += 1
    nota.notas[nota.id_actual] = {
        "titulo": titulo,
         "descripcion": descripcion,
          "fecha_creacion": fecha_actual,
          "ultima_modificacion": fecha_actual
          }
    return nota.id_actual
def leer_notas(db):
    return list(db.notas.values())

def leer_nota(db, id_nota):
    return db.notas.get(id_nota)