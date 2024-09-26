"""Herramienta para generar gráficas"""
import os
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
from utils.system_messages import msj_error_archivo


def graph_from_csv():
    """Función para generar gráficos a partir del archivo CSV"""
    current_date = datetime.now().strftime("%Y-%m-%d")
    csv_filename = f"endpoint_log_{current_date}.csv"

    if not os.path.exists(csv_filename):
        msj_error_archivo()
        return

    df = pd.read_csv(csv_filename, encoding="latin-1", header=None)
    df.columns = ["Alias", "Inicio", "Fin",
                  "Duración", "Estado", "Archivo Generado", "Ambiente"]

    df["Duración"] = pd.to_timedelta(df["Duración"])

    df["Duración_minutos"] = df["Duración"].dt.total_seconds() / 60

    avg_duration = df.groupby("Alias")["Duración_minutos"].mean()

    plt.figure(figsize=(10, 6))
    avg_duration.plot(kind="bar")
    plt.title("Tiempo promedio de ejecución por Alias")
    plt.ylabel("Duración (minutos)")
    plt.xlabel("Alias")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()
