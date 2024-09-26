import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import json


def seleccionar_archivo():
    archivo_xls = filedialog.askopenfilename(
        title="Seleccionar archivo XLS",
        filetypes=[("Archivos de Excel", "*.xls *.xlsx")]
    )
    if archivo_xls:
        convertir_a_json(archivo_xls)


def convertir_a_json(ruta_archivo):
    try:
        # Leer el archivo XLS
        df = pd.read_excel(ruta_archivo)

        # Convertir DataFrame a JSON
        resultado_json = df.to_json(orient='records', force_ascii=False)

        # Guardar el archivo JSON
        archivo_json = filedialog.asksaveasfilename(
            title="Guardar archivo JSON",
            defaultextension=".json",
            filetypes=[("Archivos JSON", "*.json")]
        )
        if archivo_json:
            with open(archivo_json, 'w', encoding='utf-8') as file:
                file.write(json.dumps(json.loads(resultado_json),
                           indent=4, ensure_ascii=False))
            messagebox.showinfo(
                "Éxito", f"El archivo JSON ha sido guardado en {archivo_json}")
        else:
            messagebox.showwarning("Cancelado", "La conversión fue cancelada.")
    except Exception as e:
        messagebox.showerror(
            "Error", f"Hubo un error al convertir el archivo: {e}")


# Configurar la ventana principal de Tkinter
ventana = tk.Tk()
ventana.title("Convertidor de XLS a JSON")

# Botón para seleccionar archivo XLS
boton_seleccionar = tk.Button(
    ventana, text="Seleccionar archivo XLS", command=seleccionar_archivo)
boton_seleccionar.pack(pady=20)

ventana.mainloop()
