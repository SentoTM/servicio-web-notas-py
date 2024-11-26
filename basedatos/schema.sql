-- Schema de notal
CREATE TABLE IF NOT EXISTS notas (
    id INT PRIMARY KEY AUTO_INCREMENT,
    titulo TEXT NOT NULL,
    contenido TEXT NOT NULL,
    fecha_creacion TEXT NOT NULL,
    ultima_modificacion TEXT NOT NULL
)