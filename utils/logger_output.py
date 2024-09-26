"""Utileria para manejar las salidas al logger en la plataforma"""

import logging

logger = logging.getLogger("Genos")


def log_db_error(error_type):
    """Función para guardar un mensaje de error en la DB"""
    logger.error("Error en base de datos: %s", error_type)


def log_error_carga_imagen(error):
    """Función para guardar un error al cargar una imagen"""
    logger.error("Error al cargar la imagen: %s", error)


def log_error_obtener_datos(error):
    """Función para guardar un error al cargar una imagen"""
    logger.error("Error al obtener datos: %s", error)


def log_carga_pantalla(pantalla):
    """Función para guardar la carga de una pantalla"""
    logger.info("Inicializando pantalla %s", pantalla)


def log_carga_imagen():
    """Función para guardar que una imagen se ha cargado correctamente"""
    logger.info("Imagen cargada correctamente")


def log_registro_actualizado(nombre):
    """Función para guardar que un registro se ha actualizado"""
    logger.info("El registro %s ha sido actualizado", nombre)


def log_registro_nuevo(nombre):
    """Función para guardar que un registro nuevo se ha creado"""
    logger.info("El registro %s ha sido creado", nombre)


def log_obtener_datos(nombre):
    """Función para guardar que se han obtenido los datos solicitados"""
    logger.info("Datos de %s obtenidos correctamente", nombre)


def log_inicio_prueba(nombre):
    """Función para guardar que se han obtenido los datos solicitados"""
    logger.info("Iniciando prueba del endpoint %s ...", nombre)


def log_comando(nombre):
    """Función para guardar que el comando ejecutado en una prueba"""
    logger.info("Ejecutando comando: %s", nombre)


def log_reporte_generado(nombre, tiempo):
    """Función para guardar registro de reporte generado en una prueba"""
    logger.info("Se ha generado el reporte %s en %s", nombre, tiempo)


def log_reporte_descargado(nombre, tiempo):
    """Función para guardar registro de reporte descargado en una prueba"""
    logger.info("Se ha descargado el reporte %s en %s", nombre, tiempo)


def log_error_prueba(nombre, contador):
    """Función para guardar registro de error en una prueba"""
    logger.info(
        "Error en el proceso de prueba: %s después de %s intentos", nombre, contador)


def log_fin_proceso(nombre):
    """Función para guardar registro de fin de prueba"""
    logger.info("Proceso %s finalizado correctamente", nombre)


def log_reintento(reintento, contador):
    """Función para guardar registro de reintentos en prueba"""
    logger.info("Reintentando %s/%s", reintento, contador)


def log_registro_prueba(nombre):
    """Función para informar ruta donde se guarda el registro"""
    logger.info("Registro de prueba guardado en %s", nombre)


def log_buscar_registro(carpeta, nombre):
    """Función si se han encontrado registros en la búsqueda"""
    logger.info("%s encontrado en %s", nombre, carpeta)
