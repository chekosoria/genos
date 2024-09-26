"""Conector a DB"""

import os
import sqlite3
from utils.logger_output import log_db_error


class DBConnector:
    """Clase DBConnector"""

    def __init__(self):
        self.db_path = self.get_db_path()
        self.connection = self.get_connection()

    def get_db_path(self):
        """Método para obtener la ruta de la base de datos local"""
        current_directory = os.path.dirname(os.path.realpath(__file__))
        return os.path.join(current_directory, "../genos.db")

    def get_connection(self):
        """Método para obtener conexión con SQLite3"""
        return sqlite3.connect(self.db_path)

    def execute_query(self, query, params=None):
        """Método para ejecutar query"""
        try:
            with self.connection as conn:
                cursor = conn.cursor()
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                conn.commit()
                return cursor
        except sqlite3.Error as e:
            log_db_error(e)
            raise

    def fetch_all(self, query, params=None):
        """Método para obtener todos los registros en query"""
        cursor = self.execute_query(query, params)
        return cursor.fetchall()

    def fetch_one(self, query, params=None):
        """Método para obtener 1 registro en un query"""
        cursor = self.execute_query(query, params)
        return cursor.fetchone()
