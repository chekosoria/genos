"""Componente para realizar algunas acciones en la base de datos local"""

import sqlite3
from utils.db_utils import obtener_conexion
from utils.logger_output import log_db_error, log_registro_nuevo


class DbActions:
    """Clase principal de modelo para administración de endpoints"""

    def __init__(self):
        self.db_connector = obtener_conexion()

    def ejecutar_en_db(self, nombre, url, download_url):
        """Inicializar la base de datos y crear las tablas si no existen"""
        try:
            query = """INSERT INTO ambientes (nombre, url, download_url)
                       VALUES (?, ?, ?)"""
            self.db_connector.execute_query(query, (nombre, url, download_url))
            log_registro_nuevo(nombre)
        except sqlite3.Error as e:
            log_db_error(e)
        return True


ambiente = "QA"
sys_url = "https://boe2qa.enlaceint.com/"
download = "https://boe2qa.enlaceint.com/reportes/"

# Crear una instancia de DbActions
db_actions = DbActions()

# Llamar al método ejecutar_en_db con los parámetros
db_actions.ejecutar_en_db(ambiente, sys_url, download)
