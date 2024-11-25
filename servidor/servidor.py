from http.server import HTTPServer, BaseHTTPRequestHandler #httpserver es el módulo que nos permite crear un servidor web, BaseHTTPRequestHandler es la clase que nos permite crear un servidor web
import json #para las peticiones, el cuerpo será en json 
from urllib.parse import urlparse, parse_qs #urlparse para parsear la url y parse_qs para parsear los parámetros de la url

class gesNotas(BaseHTTPRequestHandler):
    def __init__(gesnotas, ges_db, *args, **kwargs):
        gesnotas.ges_db = ges_db
        super().__init__(*args, **kwargs)
    
    #Función para enviar una respuesta al cliente después de procesar una petición
    def _send_response(gesnotas, status_code, data):
        gesnotas.send_response(status_code)
        gesnotas.send_header('Content-type', 'application/json')
        gesnotas.end_headers()
        gesnotas.wfile.write(json.dumps(data).encode())
    
    #Función para manejar las peticiones POST
    def do_POST(gesnotas):
        if gesnotas.path == '/notas':
            content_length = int(gesnotas.headers['Content-Length'])
            datos_enviados = json.loads(gesnotas.rfile.read(content_length))
            #Si los campos necesarios existen, creamos la nota y devolvemos el id de la nota creada
            if 'titulo' in datos_enviados and 'descripcion' in datos_enviados:
                id_nota = gesnotas.ges_db.crear_nota(datos_enviados['titulo'], datos_enviados['descripcion'])
                gesnotas._send_response(201, {'id': id_nota})
            else:
                gesnotas._send_response(400, {'error': 'Faltan campos obligatorios'})

    def do_GET(gesnotas):
        parsed_url = urlparse(gesnotas.path)
        partes_url = parsed_url.path.split('/')
        #Si la ruta es /notas, devolvemos todas las notas
        if parsed_url.path == '/notas':
            notas = gesnotas.ges_db.leer_notas()
            gesnotas._send_response(200, notas)
        elif len(partes_url) == 3 and partes_url[1] == 'notas':
            id_nota = int(partes_url[2])
            nota = gesnotas.ges_db.leer_nota(id_nota)
            if nota:
                gesnotas._send_response(200, nota)
            else:
                gesnotas._send_response(404, {'error': 'Nota no encontrada'})
    
    def do_PUT(gesnotas):
        parsed_url = urlparse(gesnotas.path)
        partes_url = parsed_url.path.split('/')

        if len(partes_url) == 3 and partes_url[1] == 'notas':
            id_nota = int(partes_url[2])
            contenido_tam = int(gesnotas.headers['Content-Length'])
            datos_modificacion = json.loads(gesnotas.rfile.read(contenido_tam))

            if 'titulo' in datos_modificacion and 'descripcion' in datos_modificacion:
                if gesnotas.ges_db.actualizar_nota(id_nota, datos_modificacion['titulo'], datos_modificacion['descripcion']):
                    gesnotas._send_response(200, {'mensaje': 'Nota actualizada'})
                else:
                    gesnotas._send_response(404, {'error': 'Nota no encontrada'})
            else:
                gesnotas._send_response(400, {'error': 'Faltan campos obligatorios'})   

    def do_DELETE(gesnotas):
        parsed_url = urlparse(gesnotas.path)
        partes_url = parsed_url.path.split('/')

        if len(partes_url) == 3 and partes_url[1] == 'notas':
            id_nota = int(partes_url[2])
            if gesnotas.ges_db.eliminar_nota(id_nota):
                gesnotas._send_response(200, {'mensaje': 'Nota eliminada'})
            else:
                gesnotas._send_response(404, {'error': 'Nota no encontrada'})

    
