from http.server import HTTPServer
from basedatos.ges_bd import GestorBD
from servidor.servidor import gesNotas

#Función para iniciar el servidor
def run(server_class=HTTPServer, port=8000):
    ges_db = GestorBD()
    #Creamos una instancia de la clase GestorBD y la pasamos al constructor de la clase gesNotas
    gestor = lambda *args, **kwargs: gesNotas(ges_db, *args, **kwargs)
    direccion_servidor = ('', port)
    #Creamos una instancia de la clase HTTPServer y la iniciamos
    httpd = server_class(direccion_servidor, gestor)
    print(f"Servidor iniciado en el puerto {port}")
    httpd.serve_forever()

run()