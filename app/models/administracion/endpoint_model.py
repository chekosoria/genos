"""Módelo para administración de endpoints"""

import sqlite3
from utils.db_utils import obtener_conexion
from utils.logger_output import log_db_error, log_registro_nuevo, log_registro_actualizado


class EndpointModel:
    """Clase principal de modelo para administración de endpoints"""

    def __init__(self):
        self.db_connector = obtener_conexion()

    def obtener_todos(self):
        """Método para obtener todos los registros"""
        try:
            query = """SELECT id,
                              nombre,
                              url,
                              parametros,
                              download_url,
                              ambiente,
                              tipo_archivo
                              FROM endpoints"""
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

    def guardar_nuevo(self, nombre, url, parametros, download_url, ambiente, tipo_archivo):
        """Método para guardar nuevo registro"""
        if nombre:
            try:
                query = """INSERT INTO endpoints (nombre,
                                                  url,
                                                  parametros,
                                                  download_url,
                                                  ambiente,
                                                  tipo_archivo) VALUES (?,?,?,?,?,?)"""
                self.db_connector.execute_query(
                    query, (nombre, url, parametros, download_url, ambiente, tipo_archivo))
                log_registro_nuevo(nombre)
            except sqlite3.Error as e:
                log_db_error(e)

    def actualizar(self, id_endpoint, nombre, url, parametros,
                   download_url, ambiente, tipo_archivo):
        """Método para actualizar registro"""
        try:
            query = """UPDATE endpoints SET nombre = ?,
                                            url = ?,
                                            parametros = ? ,
                                            download_url = ? ,
                                            ambiente = ? ,
                                            tipo_archivo = ?
                                            WHERE id = ?"""
            self.db_connector.execute_query(
                query, (nombre, url, parametros, download_url, ambiente, tipo_archivo, id_endpoint))
            log_registro_actualizado(nombre)
        except sqlite3.Error as e:
            log_db_error(e)
