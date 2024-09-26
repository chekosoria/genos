"""Vista pantalla pruebas de reportes"""
import tkinter as tk
from tkinter import ttk, END
import os
import subprocess
from datetime import datetime, timedelta
from PIL import Image, ImageTk
from app.controllers.pruebas.pruebas_reportes_controller import PruebasReportesController
from utils.db_utils import inicializar_base_de_datos
from utils.logger_output import log_carga_pantalla, log_inicio_prueba, log_comando
from utils.logger_output import log_reporte_generado, log_error_prueba
from utils.logger_output import log_fin_proceso, log_reintento
from utils.system_messages import msj_prueba_finalizada, msj_error_seleccion
from utils.files_tools import result_to_csv
from utils.graphs_tools import graph_from_csv


class PruebasReportesView(tk.Frame):
    """Pantalla para probar reportes"""

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        pantalla = "Pruebas de reportes"
        log_carga_pantalla(pantalla)

        self.controller = PruebasReportesController()

        container = tk.Frame(self)
        container.pack(expand=True, fill="both")

        label_titulo = tk.Label(container, text="Pruebas de reportes",
                                font=("Helvetica", 24, "bold"))
        label_titulo.grid(row=0, columnspan=3, pady=5, sticky="n")

        self.label_select = tk.Label(
            container, text="Seleccionar reporte(s):", font=("Helvetica", 12, "bold"))

        base_directory = os.path.abspath(os.path.join(
            os.path.dirname(__file__), '..', '..'))

        media_directory = os.path.join(base_directory, 'media')

        execute_icon_path = os.path.join(media_directory, "play.png")
        execute_image = Image.open(execute_icon_path)
        execute_icon = ImageTk.PhotoImage(execute_image)
        icon_clean_path = os.path.join(media_directory, "clean.png")
        clean_image = Image.open(icon_clean_path)
        clean_icon = ImageTk.PhotoImage(clean_image)
        graph_icon_path = os.path.join(media_directory, "graph.png")
        graph_image = Image.open(graph_icon_path)
        graph_icon = ImageTk.PhotoImage(graph_image)

        self.button_execute = tk.Button(
            container, image=execute_icon, command=self.test_reports)
        self.button_clean = tk.Button(
            container, image=clean_icon, command=self.clean_console)
        self.button_graph = tk.Button(
            container, image=graph_icon, command=graph_from_csv)

        self.button_execute.image = execute_icon
        self.button_clean.image = clean_icon
        self.button_graph.image = graph_icon

        self.mini_console = tk.Text(container, height=10, width=70)
        self.mini_console.configure(bg="black", fg="white")

        self.tree_reports = ttk.Treeview(container, columns=(
            "ID", "Nombre", "Reporte", "URL", "Ambiente"),
            show='headings', selectmode="extended")
        self.tree_reports.heading("ID", text="ID")
        self.tree_reports.heading("Nombre", text="Nombre")
        self.tree_reports.heading("Reporte", text="Reporte")
        self.tree_reports.heading("URL", text="URL")
        self.tree_reports.heading("Ambiente", text="Ambiente")
        self.tree_reports.column("ID", width=50)
        self.tree_reports.column("Nombre", width=150)
        self.tree_reports.column("Reporte", width=150)
        self.tree_reports.column("URL", width=150)
        self.tree_reports.column("Ambiente", width=150)

        self.label_select.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.tree_reports.grid(
            row=2, columnspan=3, padx=5, pady=5, sticky="nsew")
        self.button_execute.grid(row=3, column=0, pady=5, sticky="e")
        self.button_clean.grid(row=3, column=1, pady=5, sticky="w")
        self.button_graph.grid(row=3, column=2, pady=5, sticky="e")
        self.mini_console.grid(row=4, column=0, columnspan=3,
                               padx=5, pady=5, sticky="nsew")

        inicializar_base_de_datos()

        self.clean_console()
        self.clean_tree()
        self.cargar_registros()

        container.grid_rowconfigure(0, weight=0)
        container.grid_rowconfigure(1, weight=0)
        container.grid_rowconfigure(2, weight=0)
        container.grid_rowconfigure(3, weight=0)
        container.grid_rowconfigure(4, weight=0)
        container.grid_columnconfigure(0, weight=1)
        container.grid_columnconfigure(1, weight=1)
        container.grid_columnconfigure(2, weight=1)

        self.selected_id = None

        self.bind("<<ShowFrame>>", self.on_show_frame)

    def on_show_frame(self, _):
        """Cargar registros existentes desde la base de datos al mostrar la pantalla"""
        self.clean_tree()
        self.cargar_registros()

    def cargar_registros(self):
        """Cargar registros existentes desde la base de datos"""
        rows = self.controller.obtener_registros()
        for row in rows:
            self.tree_reports.insert("", tk.END, values=row)

    def test_reports(self):
        """Función para probar reportes"""
        selected_items = self.tree_reports.selection()
        if not selected_items:
            msj_error_seleccion()
            return

        for item in selected_items:
            report_values = self.tree_reports.item(item, "values")
            alias = report_values[1]
            reporte = report_values[2]
            url = report_values[3]
            env = report_values[4]
            start_time = datetime.now()
            self.mini_console.insert(
                tk.END, f"Iniciando prueba del reporte {alias}...\n")
            log_inicio_prueba(alias)
            self.mini_console.see(tk.END)
            self.master.update()
            contador_reintento = 3
            reintento = 0
            success = False
            while reintento < contador_reintento and not success:
                try:
                    created_file = reporte
                    command = ["curl", "-o", created_file,
                               "-k", url]
                    self.mini_console.insert(
                        tk.END, f"Ejecutando comando: {command}...\n")
                    log_comando(command)
                    process = subprocess.Popen(
                        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    stdout, stderr = process.communicate()
                    if process.returncode == 0:
                        end_time = datetime.now()
                        elapsed_time_seconds = (
                            end_time - start_time).total_seconds()

                        elapsed_timedelta = timedelta(
                            seconds=elapsed_time_seconds)
                        elapsed_time_formatted = str(elapsed_timedelta)

                        self.mini_console.insert(END, f"Se ha generado el reporte {
                            alias} en {elapsed_time_formatted}\n")

                        log_reporte_generado(alias, elapsed_time_formatted)

                        process_status = "Descargado"

                        self.controller.guardar_resultados(alias,
                                                           start_time,
                                                           end_time,
                                                           elapsed_time_formatted,
                                                           process_status,
                                                           created_file,
                                                           env)

                        result_to_csv(
                            alias,
                            start_time,
                            end_time,
                            elapsed_time_formatted,
                            process_status,
                            created_file,
                            env
                        )

                        success = True

                    else:

                        self.mini_console.insert(END, f"Error en el proceso de prueba: {
                            alias} después de {
                            contador_reintento} reintentos\n")
                        log_error_prueba(alias, contador_reintento)

                        reintento += 1
                        if reintento < contador_reintento:
                            self.mini_console.insert(
                                END, f"Reintentando ({reintento}/{contador_reintento})...\n")
                except subprocess.SubprocessError as e:

                    self.mini_console.insert(
                        END, f"Error en el proceso de prueba: {
                            e} después de {
                            contador_reintento} reintentos\n")
                    log_error_prueba(e, contador_reintento)

                    reintento += 1
                    if reintento < contador_reintento:

                        log_reintento(reintento, contador_reintento)

                        self.mini_console.insert(
                            END, f"Reintentando ({reintento}/{contador_reintento})...\n")

            if not success:

                self.mini_console.insert(END, f"Error en el proceso de prueba: {
                    alias} después de {contador_reintento} intentos.\n")
                log_error_prueba(alias, contador_reintento)

        self.mini_console.insert(
            END, f"Proceso {alias} finalizado correctamente\n")
        log_fin_proceso(alias)
        msj_prueba_finalizada()

    def clean_console(self):
        """Limpiar mini_console"""
        self.mini_console.delete('1.0', END)

    def clean_tree(self):
        """Limpiar mini_console"""
        self.tree_reports.delete(
            *self.tree_reports.get_children())
