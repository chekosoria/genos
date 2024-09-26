"""Vista pantalla Endpoints"""
import tkinter as tk
from tkinter import ttk
import sqlite3
import customtkinter as ctk
from app.controllers.administracion.endpoint_controller import EndpointController
from utils.db_utils import inicializar_base_de_datos
from utils.logger_output import log_carga_pantalla
from utils.system_messages import msj_registro_actualizado, msj_nuevo_registro
from utils.system_messages import msj_datos_incompletos
from utils.system_messages import msj_error_actualizar_registro, msj_error_nuevo_registro


class EndpointView(ctk.CTkFrame):
    """Pantalla para administración de Endpoints"""

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        pantalla = "Administración de endpoints"
        log_carga_pantalla(pantalla)

        self.controller = EndpointController()

        container = ctk.CTkFrame(self)
        container.pack(expand=True, fill="both")

        label_titulo = ctk.CTkLabel(container, text="Administración de endpoints",
                                    font=("Helvetica", 24, "bold"))
        label_titulo.grid(row=0, columnspan=3, pady=5, sticky="n")

        self.label_id = ctk.CTkLabel(
            container, text="ID del endpoint:", font=("Helvetica", 12, "bold"))
        self.label_id_value = ctk.CTkLabel(
            container, font=("Helvetica", 12, "bold"))
        self.label_nombre = ctk.CTkLabel(
            container, text="Nombre del endpoint:", font=("Helvetica", 12, "bold"))
        self.entry_nombre = ctk.CTkEntry(container, width=30)
        self.label_ambiente = ctk.CTkLabel(
            container, text="Ambiente:", font=("Helvetica", 12, "bold"))
        self.combobox_ambiente = ctk.CTkComboBox(
            container, width=30, state="readonly", values=["None"])
        self.combobox_ambiente.set("None")
        self.label_url = ctk.CTkLabel(
            container, text="URL:", font=("Helvetica", 12, "bold"))
        self.combobox_url = ctk.CTkComboBox(
            container, width=30, state="readonly", values=["None"])
        self.combobox_url.set("None")
        self.label_parametros = ctk.CTkLabel(
            container, text="Parámetros:", font=("Helvetica", 12, "bold"))
        self.entry_parametros = ctk.CTkEntry(container, width=30)
        self.label_download_url = ctk.CTkLabel(
            container, text="URL descarga:", font=("Helvetica", 12, "bold"))
        self.combobox_download_url = ctk.CTkComboBox(
            container, width=30, state="readonly", values=["None"])
        self.combobox_download_url.set("None")
        self.label_tipo_archivo = ctk.CTkLabel(
            container, text="Tipo de archivo:", font=("Helvetica", 12, "bold"))
        self.combobox_tipo_archivo = ctk.CTkComboBox(
            container, width=30, state="readonly", values=["None", "XLS", "PDF"])
        self.combobox_tipo_archivo.set("None")

        self.button_add_endpoint = ctk.CTkButton(
            container,
            text="Guardar",
            fg_color="#27ae60",
            hover_color="#05771e",
            font=("Montserrat", 16),
            corner_radius=12,
            width=100,
            command=self.guardar_cambios)
        self.button_cancel = ctk.CTkButton(
            container,
            text="Cancelar",
            fg_color="#ec1818",
            hover_color="#631515",
            font=("Montserrat", 16),
            corner_radius=12,
            width=100,
            command=self.cancelar_edicion)
        self.button_clean = ctk.CTkButton(
            container,
            text="Limpiar",
            fg_color="#2147f0",
            hover_color="#133b66",
            font=("Montserrat", 16),
            corner_radius=12,
            width=100,
            command=self.limpiar_formulario)

        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=(
            'Calibri', 11), background="black",
            fieldbackground="black", foreground="white")  # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=(
            'Calibri', 13, 'bold'))  # Modify the font of the headings
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {
                     'sticky': 'nswe'})])  # Remove the borders

        self.tree_endpoint = ttk.Treeview(container, columns=(
            "ID", "Nombre", "URL", "Parámetros", "URL Descarga", "Ambiente", "Tipo archivo"),
            show='headings', style="mystyle.Treeview")
        self.tree_endpoint.heading("ID", text="ID")
        self.tree_endpoint.heading("Nombre", text="Nombre")
        self.tree_endpoint.heading("URL", text="URL")
        self.tree_endpoint.heading("Parámetros", text="Parámetros")
        self.tree_endpoint.heading("URL Descarga", text="URL Descarga")
        self.tree_endpoint.heading("Ambiente", text="Ambiente")
        self.tree_endpoint.heading("Tipo archivo", text="Tipo archivo")
        self.tree_endpoint.column("ID", width=50)
        self.tree_endpoint.column("Nombre", width=150)
        self.tree_endpoint.column("URL", width=150)
        self.tree_endpoint.column("Parámetros", width=150)
        self.tree_endpoint.column("URL Descarga", width=150)
        self.tree_endpoint.column("Ambiente", width=150)
        self.tree_endpoint.column("Tipo archivo", width=150)
        self.tree_endpoint.bind("<Double-1>", self.on_double_click)

        self.label_id.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.label_id_value.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        self.label_nombre.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.entry_nombre.grid(row=3, columnspan=3,
                               padx=5, pady=5, sticky="nsew")
        self.label_ambiente.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.combobox_ambiente.grid(
            row=5, column=0, padx=5, pady=5, sticky="nsew")
        self.label_url.grid(row=6, column=0, padx=5, pady=5, sticky="w")
        self.combobox_url.grid(
            row=7, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
        self.label_parametros.grid(row=8, column=0, padx=5, pady=5, sticky="w")
        self.entry_parametros.grid(
            row=9, columnspan=3, padx=5, pady=5, sticky="nsew")
        self.label_download_url.grid(
            row=10, column=0, padx=5, pady=5, sticky="w")
        self.combobox_download_url.grid(
            row=11, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
        self.label_tipo_archivo.grid(
            row=12, column=0, padx=5, pady=5, sticky="w")
        self.combobox_tipo_archivo.grid(
            row=13, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
        self.button_add_endpoint.grid(row=15, column=0, pady=5)
        self.button_cancel.grid(row=15, column=1, pady=5)
        self.button_clean.grid(row=15, column=2, pady=5)
        self.tree_endpoint.grid(row=16, columnspan=3,
                                padx=5, pady=5, sticky="nsew")

        inicializar_base_de_datos()

        self.cargar_registros()
        self.cargar_combobox()
        self.limpiar_formulario()

        container.grid_rowconfigure(0, weight=0)
        container.grid_rowconfigure(1, weight=0)
        container.grid_rowconfigure(2, weight=0)
        container.grid_rowconfigure(3, weight=0)
        container.grid_rowconfigure(4, weight=0)
        container.grid_rowconfigure(5, weight=0)
        container.grid_rowconfigure(6, weight=0)
        container.grid_rowconfigure(7, weight=0)
        container.grid_rowconfigure(8, weight=0)
        container.grid_rowconfigure(9, weight=0)
        container.grid_rowconfigure(10, weight=0)
        container.grid_rowconfigure(11, weight=0)
        container.grid_rowconfigure(12, weight=0)
        container.grid_rowconfigure(13, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.grid_columnconfigure(1, weight=1)
        container.grid_columnconfigure(2, weight=1)

        self.selected_id = None

        self.bind("<<ShowFrame>>", self.on_show_frame)

    def on_show_frame(self, _):
        """Cargar registros existentes desde la base de datos al mostrar la pantalla"""
        self.cargar_registros()

    def cargar_registros(self):
        """Cargar registros existentes desde la base de datos"""
        self.tree_endpoint.delete(
            *self.tree_endpoint.get_children())
        rows = self.controller.obtener_registros()
        for row in rows:
            self.tree_endpoint.insert("", tk.END, values=row)

    def cargar_combobox(self):
        """Cargar datos en los Combobox desde el controlador"""
        registros = self.controller.obtener_registros_ambientes()

        ambiente = [registro[0] for registro in registros]
        urls = [registro[1] for registro in registros]
        download_urls = [registro[2] for registro in registros]

        self.combobox_ambiente.configure(values=ambiente)
        self.combobox_url.configure(values=urls)
        self.combobox_download_url.configure(values=download_urls)

        if ambiente:
            self.combobox_ambiente.set("None")
        if urls:
            self.combobox_url.set("None")
        if download_urls:
            self.combobox_download_url.set("None")

    def on_double_click(self, _):
        """Función para manejar el doble clic en el Treeview"""
        item = self.tree_endpoint.selection()[0]
        values = self.tree_endpoint.item(item, "values")

        self.selected_id = values[0]

        self.label_id_value.configure(text=values[0])
        self.entry_nombre.delete(0, tk.END)
        self.entry_nombre.insert(0, values[1])
        self.entry_parametros.delete(0, tk.END)
        self.entry_parametros.insert(0, values[3])

        ambiente = values[5]
        if ambiente in self.combobox_ambiente['values']:
            self.combobox_ambiente.set(ambiente)
        else:
            self.combobox_ambiente.set("None")

        tipo_archivo = values[6]
        if tipo_archivo in self.combobox_tipo_archivo['values']:
            self.combobox_tipo_archivo.set(tipo_archivo)
        else:
            self.combobox_tipo_archivo.set("None")

        url = values[2]
        if url in self.combobox_url['values']:
            self.combobox_url.set(url)
        else:
            self.combobox_url.set("None")

        download_url = values[4]
        if download_url in self.combobox_download_url['values']:
            self.combobox_download_url.set(download_url)
        else:
            self.combobox_download_url.set("None")

    def guardar_cambios(self):
        """Guardar los cambios realizados en el registro"""
        nombre = self.entry_nombre.get()
        ambiente = self.combobox_ambiente.get()
        url = self.combobox_url.get()
        parametros = self.entry_parametros.get()
        download_url = self.combobox_download_url.get()
        tipo_archivo = self.combobox_tipo_archivo.get()

        if nombre:
            if self.selected_id:
                try:
                    self.controller.guardar(
                        id_endpoint=self.selected_id,
                        nombre=nombre,
                        url=url,
                        parametros=parametros,
                        download_url=download_url,
                        ambiente=ambiente,
                        tipo_archivo=tipo_archivo
                    )
                    msj_registro_actualizado(nombre)
                except sqlite3.OperationalError as e:
                    msj_error_actualizar_registro(e)
            else:
                try:
                    self.controller.guardar(
                        id_endpoint=None,
                        nombre=nombre,
                        url=url,
                        parametros=parametros,
                        download_url=download_url,
                        ambiente=ambiente,
                        tipo_archivo=tipo_archivo
                    )
                    msj_nuevo_registro(nombre)
                except sqlite3.OperationalError as e:
                    msj_error_nuevo_registro(e)

            self.limpiar_formulario()
            self.cargar_registros()
        else:
            msj_datos_incompletos()

    def cancelar_edicion(self):
        """Cancelar la edición y limpiar los campos del formulario"""
        self.limpiar_formulario()

    def limpiar_formulario(self):
        """Limpiar los campos del formulario"""
        self.label_id_value.configure(text="")
        self.entry_nombre.delete(0, tk.END)
        self.combobox_ambiente.set("None")
        self.combobox_url.set("None")
        self.entry_parametros.delete(0, tk.END)
        self.combobox_download_url.set("None")
        self.combobox_tipo_archivo.set("None")
        self.selected_id = None
