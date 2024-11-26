-- Schema de notal
CREATE TABLE IF NOT EXISTS notas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    descripcion TEXT NOT NULL,
    fecha_creacion TEXT NOT NULL,
    ultima_modificacion TEXT NOT NULL
);