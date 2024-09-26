"""Utilería para establecer conexión con base de datos local"""

from utils.db_connector import DBConnector


def inicializar_base_de_datos():
    """Inicializar la base de datos y crear las tablas si no existen"""
    db_connector = DBConnector()

    tablas = {
        "ambientes": """
            CREATE TABLE IF NOT EXISTS ambientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre varchar(15) NOT NULL,
                url TEXT NOT NULL,
                download_url TEXT NOT NULL
            )
        """,
        "endpoints": """
            CREATE TABLE IF NOT EXISTS endpoints (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre varchar(100) NOT NULL,
                url TEXT NOT NULL,
                parametros TEXT NOT NULL,
                download_url TEXT NOT NULL,
                ambiente varchar(25) NOT NULL,
                tipo_archivo varchar(10) NOT NULL
            )
        """,
        "requests": """
            CREATE TABLE IF NOT EXISTS requests (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre varchar(100) NOT NULL,
                reporte varchar(100) NOT NULL,
                url TEXT NOT NULL,
                ambiente varchar(25) NOT NULL
            )
        """,
        "resultados": """
            CREATE TABLE IF NOT EXISTS resultados (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre varchar(100) NOT NULL,
                hora_inicio TEXT NOT NULL,
                hora_fin TEXT NOT NULL,
                tiempo TEXT NOT NULL,
                estatus varchar(25) NOT NULL,
                archivo varchar(25) NOT NULL,
                ambiente varchar(25) NOT NULL
            )
        """
    }

    for comando_creacion in tablas.values():
        db_connector.execute_query(comando_creacion)


def obtener_conexion():
    """Obtener una conexión a la base de datos"""
    return DBConnector()
