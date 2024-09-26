"""Módulo para configurar el log en general de la aplicación"""
import logging


def configurar_logger():
    """Función para configurar log"""
    sistema = "Genos"

    logger = logging.getLogger(sistema)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    file_handler = logging.FileHandler(f"{sistema.lower()}.log")
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    if not logger.hasHandlers():
        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

    return logger
