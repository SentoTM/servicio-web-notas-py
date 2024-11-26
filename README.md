# Servicio Web de Notas en Python 🚀
## Descripción
Este proyecto implementa un servicio web RESTful para gestionar notas usando Python. El servicio permite crear, leer, actualizar y eliminar notas mediante peticiones HTTP.

## Prueba este proyecto.

1. Clona el repositorio:
   ```
    git clone https://github.com/tu-usuario/servicio-web-notas-py.git
   ```

3. Inicializa el servidor:
   ```
    python main.py
   ```

Usa postman en el puerto indicado (8000 por defecto)

3. Prueba los tests.
   ```
    python -m unittest tests/test_notas.py
   ```



# Componentes principales
## Base de Datos (basedatos/ges_bd.py)
- Gestiona las operaciones con SQLite
- Implementa las operaciones CRUD para las notas
- Mantiene la estructura de datos definida en schema.sql
## Servidor HTTP (servidor/servidor.py)
- Maneja las peticiones HTTP
- Implementa los métodos GET, POST, PUT y DELETE
- Procesa las respuestas en formato JSON
## Punto de Entrada (main.py)
- Inicia el servidor HTTP
- Configura la conexión con la base de datos
- Establece el puerto de escucha (por defecto: 8000)

## Funcionalidades 
### 1. Crear Nota (POST /notas)
{
    "titulo": "Mi Nota",
    "descripcion": "Contenido de la nota"
}

### 2. Leer Nota (GET /notas/)
- Devuelve lista con todas las notas y su contenido.


### 3. Leer Nota (GET /notas/{id})
- Devuelve una nota específica por su ID

### 4. Modificar Nota (PUT /notas/{id})
{
    "titulo": "Mi Nota",
    "descripcion": "Contenido de la nota"
}

### 5. Eliminar Nota (DELETE /notas/{id})
- Elimina una nota específica por su ID

## Pruebas
Pruebas creadas mediante GPT, con peticiones recursivas y cambios para eliminar errores. Se ha utilizado unittesting.
El proyecto incluye tests unitarios que verifican:
- Creación correcta de notas
- Lectura de notas existentes
- Actualización de notas
- Eliminación de notas

# Sección para Reclutadores🤖
## Decisiones Técnicas y Proceso de Desarrollo
El proyecto implementa una arquitectura clara y modular:

- Separación de responsabilidades entre base de datos, servidor y lógica de negocio
- Uso de clases independientes para cada componente principal
- Implementación RESTful siguiendo estándares HTTP

## Gestión de Base de Datos
- SQLite como motor de base de datos por su ligereza y facilidad de implementación
- Uso de context managers para manejo eficiente de conexiones
- Schema SQL separado para mejor mantenibilidad

## Desarrollo del Servidor
- Implementación sobre http.server nativo de Python
- Manejo de JSON para comunicación cliente-servidor
- Respuestas HTTP estandarizadas con códigos apropiados
## Testing y Calidad
Tests desarrollados inicialmente con asistencia de CHATGPT
Proceso iterativo de mejora mediante:
- Identificación de problemas en la implementación
- Análisis de errores específicos
- Refinamiento manual de casos de prueba
- Solución de problemas de concurrencia y gestión de recursos

