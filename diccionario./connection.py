import sqlite3


def database():
    """
    Función que conecta con la base de datos y en caso de no encontrarla, la genera.
    """
    global conn, cursor
    conn = sqlite3.connect("db_diccionario.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `diccionario` (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, palabra TEXT, descripcion TEXT, tarea TEXT, url TEXT, relaciones TEXT)"
    )
