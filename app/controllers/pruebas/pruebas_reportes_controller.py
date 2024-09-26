"""Controlador para pantalla de pruebas reportes"""

import sqlite3
from app.models.pruebas.pruebas_reportes_model import PruebasReportesModel
from utils.logger_output import log_obtener_datos, log_error_obtener_datos


class PruebasReportesController:
    """Clase del controlador pantalla de pruebas reportes"""

    def __init__(self):
        self.model = PruebasReportesModel()

    def obtener_registros(self):
        """Obtener todos los registros"""
        tipo_dato = "reportes"
        try:
            reportes = self.model.obtener_todos()
            log_obtener_datos(tipo_dato)
            return reportes if reportes else []
        except sqlite3.Error as e:
            log_error_obtener_datos(e)

    def guardar_resultados(self, nombre, hora_inicio, hora_fin, tiempo, estatus, archivo, ambiente):
        """Guardar o actualizar un registro"""
        self.model.guardar_resultado(
            nombre, hora_inicio, hora_fin, tiempo, estatus, archivo, ambiente)
        return True
