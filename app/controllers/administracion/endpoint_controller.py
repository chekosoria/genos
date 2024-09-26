"""Controlador para pantalla endpoints"""

import sqlite3
from app.models.administracion.endpoint_model import EndpointModel
from utils.logger_output import log_obtener_datos, log_error_obtener_datos


class EndpointController:
    """Clase del controlador pantalla endpoints"""

    def __init__(self):
        self.model = EndpointModel()

    def obtener_registros(self):
        """Obtener todos los registros"""
        tipo_dato = "endpoints"
        try:
            endpoints = self.model.obtener_todos()
            log_obtener_datos(tipo_dato)
            return endpoints if endpoints else []
        except sqlite3.Error as e:
            log_error_obtener_datos(e)

    def obtener_registros_ambientes(self):
        """Obtener todos los registros de ambientes"""
        tipo_dato = "ambientes"
        try:
            ambientes = self.model.obtener_ambiente()
            log_obtener_datos(tipo_dato)
            return ambientes if ambientes else []
        except sqlite3.Error as e:
            log_error_obtener_datos(e)

    def guardar(self, id_endpoint, nombre, url, parametros, download_url, ambiente, tipo_archivo):
        """Guardar o actualizar un registro"""
        if id_endpoint is None:
            self.model.guardar_nuevo(
                nombre, url, parametros, download_url, ambiente, tipo_archivo)
        else:
            self.model.actualizar(id_endpoint, nombre, url,
                                  parametros, download_url, ambiente, tipo_archivo)
        return True
