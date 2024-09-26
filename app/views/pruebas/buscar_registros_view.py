"""Vista pantalla de buscar cancelaciones"""
import os
import tkinter as tk
from tkinter import filedialog, END
import customtkinter as ctk
import pandas as pd
from utils.logger_output import log_carga_pantalla
from utils.system_messages import msj_registros_encontrados, msj_registros_no_encontrados
from utils.system_messages import msj_error_seleccion
from utils.logger_output import log_buscar_registro


class BuscarRegistrosView(ctk.CTkFrame):
    """Pantalla para buscar registros"""

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        pantalla = "Pantalla para buscar registros"
        log_carga_pantalla(pantalla)

        container = ctk.CTkFrame(self)
        container.pack(expand=True, fill="both")

        label_titulo = ctk.CTkLabel(container, text="Búsqueda de registros",
                                    font=("Helvetica", 24, "bold"))
        label_titulo.grid(row=0, columnspan=3, pady=5, sticky="n")

        label_espacio = ctk.CTkLabel(container, text="",
                                     font=("Helvetica", 24, "bold"))
        label_espacio.grid(row=1, columnspan=3, pady=5, sticky="n")

        self.select_folder_label = ctk.CTkLabel(
            container, text="Seleccione la carpeta con los archivos XLS:",
            font=("Helvetica", 12, "bold"))

        self.carpeta_label = ctk.CTkLabel(
            container, text="",
            font=("Helvetica", 12))

        self.select_file_label = ctk.CTkLabel(
            container, text="Seleccione archivos XLS con lista de registros:",
            font=("Helvetica", 12, "bold"))

        self.archivo_label = ctk.CTkLabel(
            container, text="",
            font=("Helvetica", 12))

        self.select_folder_button = ctk.CTkButton(
            container,
            text="Seleccionar carpeta",
            fg_color="#a569bd",
            hover_color="#6a1c8a",
            font=("Montserrat", 16),
            corner_radius=12,
            width=50,
            command=self.seleccionar_carpeta)
        self.select_file_button = ctk.CTkButton(
            container,
            text="Seleccionar XLS",
            fg_color="#27ae60",
            hover_color="#065427",
            font=("Montserrat", 16),
            corner_radius=12,
            width=50,
            command=self.seleccionar_archivo_xls)
        self.search_button = ctk.CTkButton(
            container,
            text="Buscar",
            fg_color="#2147f0",
            hover_color="#133b66",
            font=("Montserrat", 16),
            corner_radius=12,
            width=50,
            command=self.buscar_operaciones)
        self.clean_button = ctk.CTkButton(
            container,
            text="Limpiar consola",
            fg_color="#e67e22",
            hover_color="#994d0a",
            font=("Montserrat", 16),
            corner_radius=12,
            width=50,
            command=self.limpiar_pantalla)

        self.mini_console = tk.Text(
            container, height=10, width=70, wrap='word')
        self.mini_console.configure(bg="black", fg="white")

        self.select_folder_label.grid(row=2, column=0, padx=5, pady=5)
        self.select_folder_button.grid(row=2, column=1, padx=5, pady=5)
        self.carpeta_label.grid(row=2, column=2, padx=5, pady=5)
        self.select_file_label.grid(row=3, column=0, padx=5, pady=5)
        self.select_file_button.grid(row=3, column=1, padx=5, pady=5)
        self.archivo_label.grid(row=3, column=2, padx=5, pady=5)
        self.search_button.grid(row=4, column=1, padx=5, pady=5)
        self.mini_console.grid(row=5, column=0, columnspan=3,
                               padx=5, pady=5, sticky="nsew")
        self.clean_button.grid(row=6, column=1, padx=5, pady=5)

        self.limpiar_pantalla()

        container.grid_columnconfigure(0, weight=1)
        container.grid_columnconfigure(1, weight=1)
        container.grid_columnconfigure(2, weight=1)
        container.grid_rowconfigure(0, weight=0)
        container.grid_rowconfigure(1, weight=0)
        container.grid_rowconfigure(2, weight=0)
        container.grid_rowconfigure(3, weight=0)
        container.grid_rowconfigure(4, weight=0)
        container.grid_rowconfigure(5, weight=0)

    def seleccionar_carpeta(self):
        """Método para seleccionar carpeta"""
        carpeta = filedialog.askdirectory()
        if carpeta:
            self.carpeta_label.configure(text=carpeta)
        else:
            self.carpeta_label.configure(text="No se ha seleccionado carpeta")

    def seleccionar_archivo_xls(self):
        """Método para seleccionar archivo con registros"""
        archivo = filedialog.askopenfilename(
            filetypes=[("Archivos XLS", "*.xls *.xlsx")])
        if archivo:
            self.archivo_label.configure(text=archivo)
        else:
            self.archivo_label.configure(text="No se ha seleccionado archivo")

    def buscar_operaciones(self):
        """Método para buscar registros en archivos de la carpeta"""
        carpeta = self.carpeta_label.cget("text")
        archivo_operaciones = self.archivo_label.cget("text")

        if not carpeta or not archivo_operaciones:
            msj_error_seleccion()
            self.mini_console.insert(
                END, "No se han seleccionado los medios para comparar\n")
            return

        operaciones_df = pd.read_excel(archivo_operaciones)
        operaciones = operaciones_df.iloc[:, 0].tolist()

        encontrados = []

        for filename in os.listdir(carpeta):
            if filename.endswith(".xls") or filename.endswith(".xlsx"):
                filepath = os.path.join(carpeta, filename)
                df = pd.read_excel(filepath)

                self.mini_console.insert(END, f"Buscando en {filename}...\n")

                contenido = df.to_dict(orient='records')

                for operacion in operaciones:
                    for fila in contenido:
                        if operacion in fila.values():
                            encontrados.append(
                                f"{operacion} encontrado en {filename}")
                            log_buscar_registro(filename, operacion)
                            # break

                self.mini_console.insert(
                    END, f"Finalizada búsqueda en {filename}\n")

        if encontrados:
            msj_registros_encontrados()
        else:
            msj_registros_no_encontrados()

    def limpiar_pantalla(self):
        """Limpiar Text widget mini_console"""
        self.carpeta_label.configure(text="")
        self.archivo_label.configure(text="")
        self.mini_console.delete(1.0, END)
