"""Controlador para pantalla de pruebas de anexos por lote"""

import sqlite3
from app.models.pruebas.pruebas_anexos_model import PruebasAnexosModel
from utils.logger_output import log_obtener_datos, log_error_obtener_datos


class PruebasAnexosController:
    """Clase del controlador pantalla de pruebas de anexos por lote"""

    def __init__(self):
        self.model = PruebasAnexosModel()

    def obtener_registros(self):
        """Obtener todos los registros"""
        tipo_dato = "endpoints"
        try:
            endpoints = self.model.obtener_todos()
            log_obtener_datos(tipo_dato)
            return endpoints if endpoints else []
        except sqlite3.Error as e:
            log_error_obtener_datos(e)

    def guardar_resultados(self, nombre, hora_inicio, hora_fin, tiempo, estatus, archivo, ambiente):
        """Guardar o actualizar un registro"""
        self.model.guardar_resultado(
            nombre, hora_inicio, hora_fin, tiempo, estatus, archivo, ambiente)
        return True
