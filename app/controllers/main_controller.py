"""Controlador para gestionar la navegación entre las vistas"""
import tkinter as tk
from app.views.home_view import HomeView
from app.views.administracion.endpoint_view import EndpointView
from app.views.administracion.request_view import RequestView
from app.views.pruebas.pruebas_anexos_view import PruebasAnexosView
from app.views.pruebas.pruebas_reportes_view import PruebasReportesView
from app.views.pruebas.buscar_registros_view import BuscarRegistrosView
from utils.db_utils import inicializar_base_de_datos
from utils.system_messages import msj_show_version, msj_confirmar_salida


class MainController(tk.Tk):
    """Clase principal del controlador que gestiona las vistas"""

    def __init__(self):
        super().__init__()
        self.title("Genos")
        self.geometry("1100x840")
        self.iconbitmap("bender.ico")

        inicializar_base_de_datos()

        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)

        menu_archivo = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Archivo", menu=menu_archivo)
        menu_archivo.add_command(
            label="Inicio", command=self.mostrar_inicio)

        menu_admin = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Administración", menu=menu_admin)
        menu_admin.add_command(
            label="Endpoints", command=self.mostrar_endpoints)
        menu_admin.add_command(
            label="Solicitudes", command=self.mostrar_requests)

        menu_pruebas = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Pruebas", menu=menu_pruebas)
        menu_pruebas.add_command(
            label="Anexos", command=self.mostrar_pruebas_anexos)
        menu_pruebas.add_command(
            label="Comparar Anexos", command=self.mostrar_inicio)
        menu_pruebas.add_command(
            label="Reportes", command=self.mostrar_pruebas_reportes)
        menu_pruebas.add_command(
            label="Buscar registros", command=self.mostrar_buscar_registros)

        menu_herramientas = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Herramientas", menu=menu_herramientas)
        menu_herramientas.add_command(
            label="Comparar archivos", command=self.mostrar_inicio)
        menu_herramientas.add_command(
            label="Generar gráficas", command=self.mostrar_inicio)

        menu_ayuda = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Ayuda", menu=menu_ayuda)
        menu_ayuda.add_command(label="Acerca de...", command=msj_show_version)
        menu_ayuda.add_command(
            label="Salir", command=self.quit_app)

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.inicializar_vistas()

        self.show_frame("HomeView")

    def inicializar_vistas(self):
        """Inicializar todas las vistas y guardarlas en el diccionario de frames"""
        for F in (HomeView,
                  EndpointView,
                  RequestView,
                  PruebasAnexosView,
                  PruebasReportesView,
                  BuscarRegistrosView):
            nombre_vista = F.__name__
            frame = F(self.container, self)
            self.frames[nombre_vista] = frame
            frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, page_name):
        """Método para mostrar las páginas"""
        frame = self.frames[page_name]
        frame.tkraise()

    def mostrar_inicio(self):
        """Mostrar la vista de Pantalla de inicio"""
        self.show_frame("HomeView")

    def mostrar_endpoints(self):
        """Mostrar la vista de Endpoints"""
        self.show_frame("EndpointView")

    def mostrar_requests(self):
        """Mostrar la vista de Solicitudes"""
        self.show_frame("RequestView")

    def mostrar_pruebas_anexos(self):
        """Mostrar la vista de pruebas de Anexos"""
        self.show_frame("PruebasAnexosView")

    def mostrar_pruebas_reportes(self):
        """Mostrar la vista de pruebas de reportes"""
        self.show_frame("PruebasReportesView")

    def mostrar_buscar_registros(self):
        """Mostrar la vista de pruebas de reportes"""
        self.show_frame("BuscarRegistrosView")

    def quit_app(self):
        """Función para mostrar pedir confirmación antes de salir"""
        if msj_confirmar_salida():
            self.quit()
