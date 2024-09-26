"""Módelo para administración de solicitudes"""

import sqlite3
from utils.db_utils import obtener_conexion
from utils.logger_output import log_db_error, log_registro_nuevo, log_registro_actualizado


class RequestModel:
    """Clase principal de modelo para administración de solicitudes"""

    def __init__(self):
        self.db_connector = obtener_conexion()

    def obtener_todos(self):
        """Método para obtener todos los registros"""
        try:
            query = "SELECT id, nombre, reporte, url, ambiente FROM requests"
            return self.db_connector.fetch_all(query)
        except sqlite3.Error as e:
            log_db_error(e)

    def obtener_ambiente(self):
        """Método para obtener la información de ambientes"""
        try:
            query = "SELECT nombre, url, download_url FROM ambientes"
            return self.db_connector.fetch_all(query)
        except sqlite3.Error as e:
            log_db_error(e)

    def guardar_nuevo(self, nombre, reporte, url, ambiente):
        """Método para guardar nuevo registro"""
        if nombre:
            try:
                query = "INSERT INTO requests (nombre, reporte, url, ambiente) VALUES (?,?,?,?)"
                self.db_connector.execute_query(
                    query, (nombre, reporte, url, ambiente))
                log_registro_nuevo(nombre)
            except sqlite3.Error as e:
                log_db_error(e)

    def actualizar(self, id_request, nombre, reporte, url, ambiente):
        """Método para actualizar registro"""
        try:
            query = """UPDATE requests SET nombre = ?,
                                           reporte = ?,
                                           url = ?,
                                           ambiente = ?
                                           WHERE id = ?"""
            self.db_connector.execute_query(
                query, (nombre, reporte, url, ambiente, id_request))
            log_registro_actualizado(nombre)
        except sqlite3.Error as e:
            log_db_error(e)
