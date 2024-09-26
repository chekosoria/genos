"""Modelo convertidor de XLS a JSON"""
import json
import pandas as pd


class ConvertidorXlsAJsonModel:
    """Clase del modelo del convertidor XLS a JSON"""
    @staticmethod
    def convertir(ruta_archivo):
        """Método para convertir archivo"""
        try:
            df = pd.read_excel(ruta_archivo)

            resultado_json = df.to_json(orient='records', force_ascii=False)

            return json.dumps(json.loads(resultado_json), indent=4, ensure_ascii=False)
        except RuntimeError as e:
            raise RuntimeError(f"Error al convertir el archivo: {e}") from e
