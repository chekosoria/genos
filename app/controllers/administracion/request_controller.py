"""Controlador para pantalla solicitudes"""

import sqlite3
from app.models.administracion.request_model import RequestModel
from utils.logger_output import log_obtener_datos, log_error_obtener_datos


class RequestController:
    """Clase del controlador pantalla solicitudes"""

    def __init__(self):
        self.model = RequestModel()

    def obtener_registros(self):
        """Obtener todos los registros"""
        tipo_dato = "Solicitudes"
        try:
            solicitudes = self.model.obtener_todos()
            log_obtener_datos(tipo_dato)
            return solicitudes if solicitudes else []
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

    def guardar(self, id_request, nombre, reporte, url, ambiente):
        """Guardar o actualizar un registro"""
        if id_request is None:
            self.model.guardar_nuevo(nombre, reporte, url, ambiente)
        else:
            self.model.actualizar(id_request, nombre, reporte, url, ambiente)
        return True
