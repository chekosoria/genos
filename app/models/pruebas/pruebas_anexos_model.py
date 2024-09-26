"""Módelo para pruebas de anexos"""

import sqlite3
from utils.db_utils import obtener_conexion
from utils.logger_output import log_db_error, log_registro_nuevo


class PruebasAnexosModel:
    """Clase principal de modelo para pruebas de anexos"""

    def __init__(self):
        self.db_connector = obtener_conexion()

    def obtener_todos(self):
        """Método para obtener todos los registros"""
        try:
            query = "SELECT id, nombre, url, parametros, download_url, ambiente FROM endpoints"
            return self.db_connector.fetch_all(query)
        except sqlite3.Error as e:
            log_db_error(e)

    def guardar_resultado(self, nombre, hora_inicio, hora_fin, tiempo, estatus, archivo, ambiente):
        """Método para guardar nuevo registro"""
        if nombre:
            try:
                query = """INSERT INTO resultados (nombre,
                                                   hora_inicio,
                                                   hora_fin,
                                                   tiempo,
                                                   estatus,
                                                   archivo,
                                                   ambiente) VALUES (?,?,?,?,?,?,?)"""
                self.db_connector.execute_query(
                    query, (nombre, hora_inicio, hora_fin, tiempo, estatus, archivo, ambiente))
                log_registro_nuevo(nombre)
            except sqlite3.Error as e:
                log_db_error(e)
