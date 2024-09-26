"""Utileria para el manejo de mensajes en la plataforma"""

from tkinter import messagebox


def mostrar_confirmacion(titulo, mensaje):
    """Mostrar un mensaje de confirmación en un messagebox."""
    respuesta = messagebox.askyesno(titulo, mensaje)
    return respuesta


def msj_registro_actualizado(nombre):
    """Mensaje informativo al actualizar correctamente un registro"""
    messagebox.showinfo(
        "Éxito", f"Registro {nombre} actualizado correctamente.")


def msj_error_actualizar_registro(nombre):
    """Mensaje de error al actualizar un registro"""
    messagebox.showerror(
        "Error!", f"No se pudo actualizar el registro {nombre}")


def msj_nuevo_registro(nombre):
    """Mensaje informativo al crear correctamente un nuevo registro"""
    messagebox.showinfo(
        "Éxito", f"Registro {nombre} creado correctamente.")


def msj_error_nuevo_registro(nombre):
    """Mensaje de error al crear un nuevo registro"""
    messagebox.showerror(
        "Error!", f"No se pudo crear el registro {nombre}")


def msj_datos_incompletos():
    """Mensaje de error al intentar guardar formulario incompleto"""
    messagebox.showerror(
        "Error!", "Todos los campos son obligatorios")


def msj_error_seleccion():
    """Mensaje de error al no seleccionar registro"""
    messagebox.showerror(
        "Error!", "Seleccione por lo menos un registro")


def msj_prueba_finalizada():
    """Mensaje informativo al completar proceso correctamente"""
    messagebox.showinfo(
        "Éxito", "Prueba completada.")


def msj_error_archivo():
    """Mensaje de error al no encontrar archivo"""
    messagebox.showerror(
        "Error!", "Archivo de origen no encontrado")


def msj_show_version():
    """Función para mostrar la versión de la interfaz"""
    version = "GENOS 3.0"
    fecha = "2024-07-26"
    python_version = "Python 3.12.12"
    descripcion = "Software by Cheko"
    messagebox.showinfo("INFO", f"{version}\n{fecha}\n{
                        python_version}\n{descripcion}")


def msj_confirmar_salida():
    """Función para solicitar confirmación para salir de la aplicación"""
    return messagebox.askyesno(
        "Confirmar salida", "¿Está seguro de que desea salir?")


def msj_registros_encontrados():
    """Mensaje informativo al encontrar registros buscados"""
    messagebox.showinfo(
        "Alerta!", "Registros localizados\n")


def msj_registros_no_encontrados():
    """Mensaje informativo al no encontrar registros buscados"""
    messagebox.showinfo(
        "Resultados", "No se encontraron los registros buscados en la carpeta seleccionada")
