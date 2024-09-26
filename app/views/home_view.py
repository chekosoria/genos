"""Vista pantalla inicio"""
import logging
import os
import customtkinter as ctk
import PIL as pil
from PIL import Image
from utils.logger_output import log_carga_pantalla, log_carga_imagen, log_error_carga_imagen


class HomeView(ctk.CTkFrame):
    """Clase principal de la pantalla de inicio"""

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.logger = logging.getLogger("Genos")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        pantalla = "Pantalla de inicio"
        log_carga_pantalla(pantalla)

        label_titulo = ctk.CTkLabel(
            self, text="Bienvenido a Genos", font=("Helvetica", 24, "bold"))
        label_titulo.pack(pady=20)

        frame_imagen = ctk.CTkFrame(self)
        frame_imagen.pack(pady=20)

        current_directory = os.path.dirname(os.path.realpath(__file__))

        media_directory = os.path.join(current_directory, '..', 'media')

        image_path = os.path.join(media_directory, "bug.jpg")
        self.cargar_imagen(image_path, frame_imagen)

    def cargar_imagen(self, ruta_imagen, frame):
        """Función para cargar la imagen"""
        try:
            imagen = Image.open(ruta_imagen)
            imagen = imagen.resize((333, 331), Image.Resampling.LANCZOS)
            self.imagen_tk = ctk.CTkImage(imagen,
                                          size=(333, 331))

            imagen_label = ctk.CTkLabel(frame, image=self.imagen_tk, text="")
            imagen_label.pack()
            log_carga_imagen()
        except pil.UnidentifiedImageError as e:
            log_error_carga_imagen(e)
