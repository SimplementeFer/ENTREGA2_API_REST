# api/funciones_auxiliares.py

import html
import bleach  # Asegúrate de tener esta librería en requirements.txt

def sanitize_input(user_input):
    """
    Sanitiza la entrada de los usuarios para evitar inyecciones XSS.
    """
    escaped_input = html.escape(user_input)  # Escapa caracteres especiales en HTML
    return bleach.clean(escaped_input)  # Limpia cualquier HTML no permitido
