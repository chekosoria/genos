"""Aplicación principal"""
from app.controllers.main_controller import MainController
from utils.logging_config import configurar_logger


def main():
    """Función para llamar al controlador de interfaz"""

    configurar_logger()

    app = MainController()
    app.mainloop()


if __name__ == "__main__":
    main()
