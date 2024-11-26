import unittest
import sys
import os
import json
import sqlite3
from http.client import HTTPConnection
from http.server import HTTPServer
import threading
import time

from basedatos.ges_bd import GestorBD
from servidor.servidor import gesNotas

class TestNotasAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Inicializamos base de datos
        cls.ges_db = GestorBD("test_notas.db")
        
        # Aseguramos limpieza base de datos de pruebas
        with sqlite3.connect("test_notas.db") as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM notas")
            cursor.execute("DELETE FROM sqlite_sequence")  # Reseteamos autoincremento
            conn.commit()
        
        # Iniciamos servidor de pruebas
        def handler(*args):
            return gesNotas(cls.ges_db, *args)
        
        cls.server = HTTPServer(('localhost', 8000), handler)
        cls.server_thread = threading.Thread(target=cls.server.serve_forever)
        cls.server_thread.daemon = True
        cls.server_thread.start()
        time.sleep(1)
    def setUp(self):

        # Nueva conexión para cada test
        self.conn = HTTPConnection('localhost', 8000)
        
    def test_1_crear_nota(self):
        datos = {
            "titulo": "Test Nota",
            "descripcion": "Descripción de prueba"
        }
        self.conn.request('POST', '/notas', json.dumps(datos))
        response = self.conn.getresponse()
        
        self.assertEqual(response.status, 201)
        respuesta = json.loads(response.read().decode())
        self.assertIn('id', respuesta)
        self.assertEqual(respuesta['id'], 1)

    def test_2_leer_nota(self):
        self.conn.request('GET', '/notas/1')
        response = self.conn.getresponse()
        
        self.assertEqual(response.status, 200)
        nota = json.loads(response.read().decode())
        self.assertEqual(nota['titulo'], "Test Nota")
        self.assertEqual(nota['descripcion'], "Descripción de prueba")

    def test_3_actualizar_nota(self):
        datos_actualizacion = {
            "titulo": "Nota Actualizada",
            "descripcion": "Nueva descripción"
        }
        self.conn.request('PUT', '/notas/1', json.dumps(datos_actualizacion))
        response = self.conn.getresponse()
        
        self.assertEqual(response.status, 200)
        
        # Verificamos modificación
        self.conn.request('GET', '/notas/1')
        response = self.conn.getresponse()
        nota = json.loads(response.read().decode())
        self.assertEqual(nota['titulo'], "Nota Actualizada")

    def test_4_eliminar_nota(self):
        self.conn.request('DELETE', '/notas/1')
        response = self.conn.getresponse()
        
        self.assertEqual(response.status, 200)
        
        # Verificamos eliminación
        self.conn.request('GET', '/notas/1')
        response = self.conn.getresponse()
        self.assertEqual(response.status, 404)

    def tearDown(self):
        # Cerramos conexión para evitar resourcewarning
        self.conn.close()

    @classmethod
    def tearDownClass(cls):
        # Limpieza de servidor y base de datos
        cls.server.shutdown()
        cls.server.server_close()
        time.sleep(1)  
        try:
            os.remove("test_notas.db")
        except PermissionError:
            pass 

if __name__ == '__main__':
    unittest.main()
