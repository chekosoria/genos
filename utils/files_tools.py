"""Herramientas para manejo de archivos"""
import csv
from datetime import datetime
from utils.logger_output import log_registro_prueba


def result_to_csv(alias, start_time, end_time, elapsed_time_formatted,
                  status, generated_filename, env):
    """Función para almacenar el resultado de la prueba en un CSV"""
    current_date = datetime.now().strftime("%Y-%m-%d")
    csv_filename = f"endpoint_log_{current_date}.csv"
    with open(csv_filename, 'a', newline='', encoding="latin-1") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([alias, start_time.strftime("%H:%M:%S"), end_time.strftime(
            "%H:%M:%S"), elapsed_time_formatted, status, generated_filename, env])

    log_registro_prueba(csv_filename)
