"""Controlador del convertidor XLS a JSON"""
from app.models.herramientas.xls_a_json_model import ConvertidorXlsAJsonModel


class ConvertidorXlsAJsonController:
    """Clase del controlador del convertidor xls a json"""

    def __init__(self, vista):
        self.vista = vista

    def convertir_a_json(self, ruta_archivo):
        """Método para convertir"""
        try:
            resultado_json = ConvertidorXlsAJsonModel.convertir(ruta_archivo)

            archivo_json = self.vista.mostrar_guardar_como()
            if archivo_json:
                with open(archivo_json, 'w', encoding='utf-8') as file:
                    file.write(resultado_json)
                self.vista.mostrar_mensaje_exito(archivo_json)
            else:
                self.vista.mostrar_mensaje_error(
                    "La conversión fue cancelada.")
        except RuntimeError as e:
            self.vista.mostrar_mensaje_error(str(e))
